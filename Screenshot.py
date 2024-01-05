import os
import time
import tkinter as tk
import pyautogui
import datetime


root = tk.Tk()
root.title("Browser")
root.geometry('90x70')
root.config(bg='#AAE7FD')
root.minsize(90, 65)
root.maxsize(90, 65)


def main():
    def File():
        os.startfile(r'Screenshot')

    def Screenshot():
        FileName = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        img = pyautogui.screenshot()
        if 'Screenshot' not in os.listdir():
            os.makedirs('Screenshot')
        img.save(fr"Screenshot\{FileName}.png")
        print(f"I'm done sir, Your screenshot saved.")
        time.sleep(1)

    def OnTopScreen():
        current_state = onTop.get()
        root.attributes('-topmost', current_state)

    onTop = tk.BooleanVar()
    onTop.set(False)

    selected_option = tk.StringVar()
    selected_option.set('Settings')

    b1 = tk.Button(root, text="File", fg="White", bg="#3b5998", font=('Comic Sans MS', 10), command=File)
    b2 = tk.Button(root, text="Screenshot", font=('Comic Sans MS', 10), fg="White", bg="#3b5998", command=Screenshot)
    # dropMenu = tk.OptionMenu(root, selected_option, *lan)
    check_button = tk.Checkbutton(root, text="Top", variable=onTop, relief='ridge', command=OnTopScreen, bg="#AAE7FD")

    b1.place(x=70, y=5, height=25, width=40)
    b2.place(x=10, y=33, height=25, width=100)

    check_button.place(x=10, y=5, )

    root.mainloop()


if __name__ == '__main__':
    main()
