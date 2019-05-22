from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Викторина")
root.geometry("500x500")


def que_1():
    question_1 = Label(root, text="Виисит груша нельзя скушать")
    answer_1 = Entry()
    btn = Button(root, text="Нажми что бы проверить", bg="red", command=lambda: game1())
    question_1.grid(row=0)
    answer_1.grid(row=1)
    btn.grid(row=3)

    def game1():
        if answer_1.get().lower() == "лампочка":
            que_2()
        else:
            messagebox.showerror("Неверно", "попробуй еще раз!")


def que_2():
    question_1 = Label(root, text="Зимой и летом одним цветом")
    answer_1 = Entry()
    btn = Button(root, text="Нажми что бы проверить", bg="green", command=lambda: game2())
    question_1.grid()
    answer_1.grid()
    btn.grid()

    def game2():
        if answer_1.get().lower() == "ёлка":
            messagebox.showinfo("Победа!", "Ты выиграл")
        else:
            messagebox.showerror("Неверно", "попробуй еще раз!")


que_1()


root.mainloop()