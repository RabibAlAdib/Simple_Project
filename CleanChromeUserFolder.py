import os
import shutil
import sys

def get_size(path):
    """Calculate total size of files/folders in bytes"""
    total = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total += os.path.getsize(fp)
                except:
                    continue
    return total

def format_size(size_bytes):
    """Convert bytes to human-readable format"""
    if size_bytes == 0:
        return "0B"
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names)-1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.2f}{size_names[i]}"

def clean_chrome_profile(profile_path, is_critical_profile=False):
    """Clean unnecessary files from a Chrome profile"""
    critical_files = {
        'Cookies', 'Cookies-journal', 'Login Data', 'Login Data For Account',
        'Web Data', 'Web Data-journal', 'Preferences', 'Secure Preferences'
    }
    
    cleanable_items = {
        'Cache', 'GPUCache', 'Media Cache', 'Code Cache',
        'History', 'History-journal', 'Archived History',
        'Current Session', 'Current Tabs', 'Last Session', 'Last Tabs',
        'Temp', 'Service Worker', 'Storage', 'Thumbnails',
        'Visited Links', 'Web Applications', 'DawnCache', 'ShaderCache'
    }
    
    freed_space = 0
    removed_items = []
    
    if not os.path.isdir(profile_path):
        return 0, []
    
    for item in os.listdir(profile_path):
        item_path = os.path.join(profile_path, item)
        
        # Skip critical files for protected profile
        if is_critical_profile and item in critical_files:
            continue
            
        # Clean all non-critical items
        if item in cleanable_items:
            try:
                size = get_size(item_path)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
                freed_space += size
                removed_items.append(item)
            except Exception as e:
                print(f"Error removing {item}: {str(e)}")
    
    return freed_space, removed_items

def main():
    base_path = r"C:\Users\rabib\AppData\Local\Google\Chrome\User Data"
    critical_profile = "Profile 41"
    total_freed = 0
    all_removed = []
    
    print("Chrome Browser Cleaner")
    print("=" * 40)
    
    # Verify base path exists
    if not os.path.isdir(base_path):
        print(f"Error: Chrome user data not found at {base_path}")
        sys.exit(1)
    
    # Process all profiles
    for profile in os.listdir(base_path):
        profile_path = os.path.join(base_path, profile)
        if os.path.isdir(profile_path) and (profile.startswith("Profile ") or profile == "Default"):
            is_critical = (profile == critical_profile)
            freed, removed = clean_chrome_profile(profile_path, is_critical)
            total_freed += freed
            all_removed.extend([f"{profile}/{item}" for item in removed])
            
            status = "PROTECTED" if is_critical else "CLEANED"
            print(f"\n[{status}] {profile}: {format_size(freed)} freed")
    
    # Summary report
    print("\n" + "=" * 40)
    print(f"Total space freed: {format_size(total_freed)}")
    print(f"Items removed: {len(all_removed)}")
    
    if all_removed:
        print("\nRemoved items:")
        for item in all_removed[:10]:  # Show first 10 items
            print(f"  - {item}")
        if len(all_removed) > 10:
            print(f"  ... and {len(all_removed)-10} more")

if __name__ == "__main__":
    main()
    