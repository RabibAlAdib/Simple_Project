import os
import sys
import threading
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ---------- Utilities ----------
def format_size(size):
    """Convert bytes to human readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} EB"

def get_folder_size(path):
    """Compute folder size (sum of all files). Uses os.walk; exceptions are ignored."""
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                try:
                    fp = os.path.join(dirpath, f)
                    if os.path.islink(fp):
                        continue
                    total += os.path.getsize(fp)
                except Exception:
                    pass
    except Exception:
        pass
    return total

def open_path_with_default(path):
    """Open a file or folder with the OS default application."""
    if not os.path.exists(path):
        messagebox.showerror("Error", f"Path not found:\n{path}")
        return
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.run(["open", path], check=False)
        else:
            subprocess.run(["xdg-open", path], check=False)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open path:\n{e}")

# ---------- GUI App ----------
class DirSizeApp:
    def __init__(self, root):
        self.root = root
        root.title("Directory Size Viewer")
        root.geometry("900x550")

        self.directory_var = tk.StringVar()
        self.pin_var = tk.BooleanVar()
        self.scanning = False
        self.scan_thread = None

        # Caching and navigation
        # cache: path -> list of items where each item is dict {name, type, size, fullpath}
        self.cache = {}
        # history stack of visited paths (for Back)
        self.history = []
        # current displayed directory path
        self.current_dir = ""

        # Top controls
        top = ttk.Frame(root)
        top.pack(fill="x", padx=10, pady=8)

        ttk.Label(top, text="Directory:").pack(side="left")
        self.entry = ttk.Entry(top, textvariable=self.directory_var, width=70)
        self.entry.pack(side="left", padx=6)
        self.entry.bind("<Return>", lambda e: self.start_scan())
        # global paste bindings
        self.entry.bind_all("<Control-v>", self._on_ctrl_v)
        self.entry.bind_all("<Control-V>", self._on_ctrl_v)
        self.entry.bind_all("<Command-v>", self._on_ctrl_v)

        ttk.Button(top, text="Browse", command=self.choose_directory).pack(side="left", padx=(4,0))
        ttk.Button(top, text="Scan", command=self.start_scan).pack(side="left", padx=(6,0))
        ttk.Button(top, text="Paste & Scan", command=self.paste_and_scan).pack(side="left", padx=(6,0))

        # navigation buttons
        ttk.Button(top, text="Back", command=self.go_back).pack(side="left", padx=(12,0))
        ttk.Button(top, text="Up", command=self.go_up).pack(side="left", padx=(6,0))

        ttk.Checkbutton(top, text="Pin to Top", variable=self.pin_var, command=self.toggle_pin).pack(side="left", padx=8)

        # Progress and status
        progress_frame = ttk.Frame(root)
        progress_frame.pack(fill="x", padx=10, pady=(0,6))

        self.progress = ttk.Progressbar(progress_frame, orient="horizontal", mode="determinate")
        self.progress.pack(fill="x", side="left", expand=True)

        self.status_label = ttk.Label(progress_frame, text="Idle")
        self.status_label.pack(side="left", padx=8)

        # Treeview for results
        self.tree = ttk.Treeview(root, columns=("Name", "Type", "Size"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Size", text="Size")
        self.tree.column("Name", anchor="w", width=620)
        self.tree.column("Type", anchor="center", width=100)
        self.tree.column("Size", anchor="e", width=140)
        self.tree.pack(fill="both", expand=True, padx=10, pady=(0,10))

        # Bind double-click to open/explore
        self.tree.bind("<Double-1>", self._on_double_click)
        # Right-click menu
        self.tree.bind("<Button-3>", self._on_right_click)

        # Keep a map from tree iid to full path for quick open (cleared whenever view changes)
        self._iid_to_path = {}

    # ---------- Clipboard helpers ----------
    def _on_ctrl_v(self, event=None):
        try:
            clip = self.root.clipboard_get()
            self.directory_var.set(clip)
        except Exception:
            pass
        return "break"

    def paste_and_scan(self):
        try:
            clip = self.root.clipboard_get()
            if clip:
                self.directory_var.set(clip)
                if os.path.isdir(clip):
                    self.start_scan()
                else:
                    self.status_label.config(text="Pasted (not a directory)")
        except Exception:
            messagebox.showinfo("Clipboard", "No text found in clipboard.")

    # ---------- Directory / scanning ----------
    def toggle_pin(self):
        self.root.attributes("-topmost", self.pin_var.get())

    def choose_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.directory_var.set(folder)

    def start_scan(self):
        """Scan the given directory and set it as the current view (clears history)."""
        path = self.directory_var.get().strip()
        if not path:
            messagebox.showerror("Error", "Please enter a directory path.")
            return
        if not os.path.isdir(path):
            messagebox.showerror("Error", "Invalid directory path.")
            return
        if self.scanning:
            messagebox.showinfo("Scanning", "Scan already in progress.")
            return

        # clear previous view and history when explicitly scanning a new main dir
        self.history.clear()
        self._display_path(path, rescan=True, push_history=True)

    def _display_path(self, path, rescan=False, push_history=False):
        """Display a directory in the tree. Use cache if available unless rescan=True.
        If push_history=True, push current_dir to history before changing."""
        if push_history and self.current_dir:
            self.history.append(self.current_dir)

        # if cached and not forced to rescan, just render cache
        if (path in self.cache) and not rescan:
            self._render_items_from_cache(path)
        else:
            # perform a scan (in background) and cache results, then render
            if self.scanning:
                messagebox.showinfo("Scanning", "Another scan is running. Try again later.")
                return
            self._start_scan_path(path)

    def _start_scan_path(self, path):
        """Threaded scanning of a path; caches and then renders."""
        # prepare UI state
        self.scanning = True
        self.progress["value"] = 0
        self.status_label.config(text="Preparing...")
        self._set_controls_state(disabled=True)

        def worker():
            items = []
            try:
                entries = []
                try:
                    with os.scandir(path) as it:
                        for entry in it:
                            entries.append(entry)
                except PermissionError:
                    self._schedule(lambda: messagebox.showerror("Error", "Permission denied scanning directory."))
                    self._finish_scan()
                    return
                except Exception as e:
                    self._schedule(lambda: messagebox.showerror("Error", f"Failed to list directory:\n{e}"))
                    self._finish_scan()
                    return

                total = len(entries)
                self._schedule(lambda: self.progress.config(maximum=max(1, total)))
                processed = 0

                for entry in entries:
                    name = entry.name
                    full_path = entry.path
                    is_dir = entry.is_dir(follow_symlinks=False)
                    size = 0
                    if is_dir:
                        size = get_folder_size(full_path)
                        typ = "Folder"
                    else:
                        try:
                            if entry.is_symlink():
                                size = 0
                            else:
                                size = entry.stat(follow_symlinks=False).st_size
                        except Exception:
                            size = 0
                        typ = "File"

                    items.append({"name": name, "type": typ, "size": size, "path": full_path})
                    processed += 1
                    self._schedule(lambda p=processed, tot=total: self._update_progress(p, tot))

                # cache results
                self.cache[path] = items
                self._schedule(lambda: self._render_items_from_cache(path))
                self._schedule(lambda: self.status_label.config(text=f"Done: {total} item(s)"))
            finally:
                self._finish_scan()

        t = threading.Thread(target=worker, daemon=True)
        t.start()

    def _render_items_from_cache(self, path):
        """Render cached items for path into the tree (no scanning)."""
        self.current_dir = path
        # clear existing tree and mapping
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        self._iid_to_path.clear()

        items = self.cache.get(path, [])
        for it in items:
            dn = it["name"]
            typ = it["type"]
            ds = format_size(it["size"])
            fp = it["path"]
            iid = self.tree.insert("", "end", values=(dn, typ, ds))
            self._iid_to_path[iid] = fp

        # update UI labels
        display = path
        self.directory_var.set(display)
        self.status_label.config(text=f"Viewing: {path} ({len(items)} item(s))")
        try:
            # make progress full visually
            self.progress.config(value=self.progress["maximum"])
        except Exception:
            pass

    def _set_controls_state(self, disabled: bool):
        state = "disabled" if disabled else "normal"
        try:
            self.entry.config(state=state)
        except Exception:
            pass
        # enable/disable buttons: Scan, Paste & Scan, Browse
        for child in self.root.winfo_children():
            for sub in child.winfo_children():
                if isinstance(sub, ttk.Button) and sub.cget("text") in ("Scan", "Paste & Scan", "Browse"):
                    try:
                        sub.config(state=state)
                    except Exception:
                        pass

    def _update_progress(self, processed, total):
        self.progress["value"] = processed
        self.status_label.config(text=f"Processed {processed}/{total}")

    def _schedule(self, fn):
        self.root.after(0, fn)

    def _finish_scan(self):
        def finish():
            self.scanning = False
            self._set_controls_state(disabled=False)
            try:
                self.progress.config(value=self.progress["maximum"])
            except Exception:
                pass
        self._schedule(finish)

    # ---------- Navigation: Explore, Back, Up ----------
    def _get_selected_item_path(self, event=None):
        iid = self.tree.focus()
        if not iid:
            if event is not None:
                iid = self.tree.identify_row(event.y)
            if not iid:
                return None
        return self._iid_to_path.get(iid)

    def _on_double_click(self, event):
        """Double-click: if folder -> explore in viewer; if file -> open with OS."""
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        full_path = self._iid_to_path.get(iid)
        if not full_path:
            return
        if os.path.isdir(full_path):
            # enter folder in viewer (push history so Back works)
            self._display_path(full_path, rescan=False, push_history=True)
        else:
            open_path_with_default(full_path)

    def _on_right_click(self, event):
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        self.tree.selection_set(iid)
        menu = tk.Menu(self.root, tearoff=0)
        full_path = self._iid_to_path.get(iid)

        def do_open():
            if full_path:
                open_path_with_default(full_path)

        def open_containing():
            if full_path:
                if os.path.isdir(full_path):
                    open_path_with_default(full_path)
                else:
                    folder = os.path.dirname(full_path)
                    open_path_with_default(folder)

        def explore_in_viewer():
            if full_path and os.path.isdir(full_path):
                self._display_path(full_path, rescan=False, push_history=True)
            elif full_path:
                messagebox.showinfo("Info", "Selected item is not a folder.")

        def copy_path():
            if full_path:
                try:
                    self.root.clipboard_clear()
                    self.root.clipboard_append(full_path)
                except Exception:
                    pass

        menu.add_command(label="Open", command=do_open)
        menu.add_command(label="Open Containing Folder", command=open_containing)
        menu.add_command(label="Explore in Viewer", command=explore_in_viewer)
        menu.add_command(label="Copy Full Path", command=copy_path)
        menu.post(event.x_root, event.y_root)

    def go_back(self):
        """Go back to last path from history without re-scanning (uses cache)."""
        if not self.history:
            messagebox.showinfo("Back", "No previous directory in history.")
            return
        prev = self.history.pop()
        # display prev using cache (do not push current to history)
        if prev in self.cache:
            self._render_items_from_cache(prev)
        else:
            # if not cached (unlikely) just scan it but do NOT modify history
            self._display_path(prev, rescan=True, push_history=False)

    def go_up(self):
        """Go to parent directory of current view. If parent is cached show it; otherwise scan it.
           Do not push current directory into history (user expects Up to move without stacking)."""
        if not self.current_dir:
            return
        parent = os.path.dirname(self.current_dir.rstrip(os.sep))
        if not parent:
            messagebox.showinfo("Up", "No parent directory.")
            return
        # If parent equals current (root), still attempt to show it
        if parent in self.cache:
            self._render_items_from_cache(parent)
        else:
            # scan parent but do not push the current dir into history
            self._display_path(parent, rescan=True, push_history=False)

# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = DirSizeApp(root)
    root.mainloop()
