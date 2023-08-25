from textblob import TextBlob
from tkinter import Tk
from tkinter import filedialog

gui = Tk()
gui.filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("txt files",
                                                      ".txt"),
                                                     ("all files", ".*")))
with open(gui.filename, 'r') as f:
    s = list(f)
for i in range(len(s)):
    s[i] = TextBlob(s[i])
    s[i] = s[i].correct()
with open(gui.filename, 'w') as f:
    for i in range(len(s)):
        s[i] = str(s[i])
        f.write(s[i])
