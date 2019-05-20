from tkinter import *

okToPressReturn = True

bomb = 100
day = 0
a = 79
def start(event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        startLabel.config(text=" ")
        updateBomb()
        updateDay()
        updateDisplay()

        okToPressReturn = False


def updateDisplay():
    global bomb
    global day
    if bomb<=50:
        bomb_normal.config(image=nophoto)
    else:
        bomb_normal.config(image=normalphoto)
    bombLabel.config(text="Time left: " + str(bomb))
    dayLabel.config(text="Day " + str(day))
    bomb_normal.after(100, updateDisplay)


def updateBomb():
    global bomb
    bomb -= 1
    if isAlive():
        bombLabel.after(500, updateBomb)


def updateDay():
    global day
    day += 1
    if isAlive():
        dayLabel.after(5000, updateDay)


def stop():
    global bomb
    global a


    if isAlive():

        if bomb <= a:
            bomb += 3

        else:
            bomb -= 20
            a -= 5




def isAlive():
    global bomb
    if bomb <= 0:
        startLabel.config(text="BOM! BOM!")
        bomb_normal.config(image=bangphoto)
        return False
    else:
        return True


root = Tk()
root.title("Bomb")
root.geometry("500x700")

startLabel = Label(root, text="Press Enter to Start", font=("Helvetica", 12))
bombLabel = Label(root, text="Time left: " + str(bomb), font=("Helvetica", 12))
dayLabel = Label(root, text="Day " + str(day), font=("Helvetica", 12))

nophoto = PhotoImage(file="bomb_no.gif")
normalphoto = PhotoImage(file="bomb_normal.gif")
bangphoto = PhotoImage(file="bang.gif")

bomb_normal = Label(root, image=normalphoto)
btn_no_bomb = Button(root, text="Press!", command=stop)


startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()



ban_photo = Label(root, image=bangphoto)


root.bind('<Return>', start)


root.mainloop()