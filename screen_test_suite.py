import tkinter as tk
from threading import Thread
from time import sleep

colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFFFF", "#000000", "#FF00FF"]

root = tk.Tk()
root.attributes('-fullscreen', True)

def close():
   root.destroy()
   root.quit()

def exit_event():
    root.bind("<Escape>", lambda x: close())

def click_event():
    root.bind("<Button-1>", lambda x: root.configure(background = list(colors)[-1]))

def colors_loop():
    while True:
        for i in range(0, len(colors) - 1):
            root.configure(background = colors[i])
            root.update()
            sleep(1)

if __name__ == "__main__":
    exit_thread = Thread(target = exit_event)
    exit_thread.setDaemon(True)
    exit_thread.start()

    click_thread = Thread(target = click_event)
    click_thread.setDaemon(True)
    click_thread.start()

    main_thread = Thread(target = colors_loop)
    main_thread.setDaemon(True)
    main_thread.start()

    root.mainloop()
