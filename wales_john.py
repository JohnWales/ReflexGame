from tkinter import *
import random
import time

global circle
global counter
counter = 0


def stop():
    root.destroy()


def cb1():
    xpos = random.randint(1, 300)
    ypos = random.randint(1, 300)
    canvas.delete(ALL)
    global circle
    circle = canvas.create_oval(xpos, ypos, xpos+40, ypos+40, fill=(random.sample(COLORS, 1)[0]))
    button.destroy()
    canvas.tag_bind(circle, "<ButtonPress-1>", deleteCircle)
    global start
    start = time.time()


def deleteCircle(event):
    global counter
    global start
    canvas.delete(ALL)
    xpos = random.randint(1, 300)
    ypos = random.randint(1, 300)
    circle = canvas.create_oval(xpos, ypos, xpos+40, ypos+40, fill=(random.sample(COLORS, 1)[0]))
    root.configure(bg=(random.sample(COLORS, 1)[0]))
    canvas.configure(bg=random.sample(COLORS, 1)[0])
    canvas.tag_bind(circle, "<ButtonPress-1>", deleteCircle)
    end = time.time()
    timeTaken = (end - start)
    if timeTaken < 2:
        counter = counter + 1
        counterLabel.config(text="Points: " + str(counter))
        formattedTime = '{0:.2f}'.format(timeTaken)
        timeLabel.config(text="Time: " + str(formattedTime))
    else:
        counter = 0
        counterLabel.config(text="Points: " + str(counter))
    start = time.time()


root = Tk()     # Main Window/Mainframe
entry = Entry(root)

COLORS = ['snow', 'red', 'lime', "aquamarine", "fuchsia", 'blue', 'yellow', 'pink']  # List of colours

canvas = Canvas(root, height=400, width=400)
canvas.pack(side=TOP)

frame = Frame(root)

button = Button(frame, text="Start", command=cb1, bg=(random.sample(COLORS, 1)[0]))   # Add Button
stopButton = Button(frame, text="Stop", command=stop, bg=(random.sample(COLORS, 1)[0]))
button.grid(row=1, column=1)
stopButton.grid(row=1, column=2)

counterLabel = Label(root, text="Points: ")   # Label to show user the number of points he/she has
counterLabel.place(x=0, y=0)

timeLabel = Label(root, text="Time: ")  # Label to show user how much time it took them to click circle
timeLabel.place(x=328, y=0)

frame.pack(side=BOTTOM)

root.mainloop()     # Wait for interaction. Start the application running
