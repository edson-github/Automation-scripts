import tkinter
import subprocess


def makenew():
    maker(numofwindows)


def maker(wins):
    global numofwindows
    subprocess.Popen(["python.exe", "note.py", str(numofwindows)], shell=True)
    numofwindows = 1 + wins
    maintain()


def maintain():
    global numofwindows
    with open("assets\\storage", "w") as storage:
        storage.write(str(numofwindows))


def reset():
    with open("assets\\storage", "w") as storage:
        storage.write(str(0))


try:
    with open("assets\\storage", "r") as getwin:
        win = getwin.readline()
        numofwindows = int(win)
    for i in range(0, numofwindows):
        subprocess.Popen(["python.exe", "note.py", str(i)], shell=True)
except FileNotFoundError:
    numofwindows = 0

manager = tkinter.Tk()
manager.title("Audio Notes - Master")

while True:
    try:
        makeNewBtn = tkinter.Button(manager, text='New+', command=makenew)
        makeNewBtn.pack()
        reset = tkinter.Button(manager, text='Reset-', command=reset)
        reset.pack()
        tkinter.mainloop()
    except tkinter.TclError:
        break
