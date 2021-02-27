import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
import image
from PIL import Image, ImageTk
from tkinter import *
import json
import random


# FirstPage

window = tk.Tk()
window.title("Test de cultura generala")
window.geometry("800x600")
window.resizable(False, False)


# FirstPage Title
def question(qn):
    title = tk.Label(window, text="Test de cultura generala", width=50, bg="purple", fg="blue",
                     font=("times", 20, "bold"))
    title.place(x=0, y=1)


class Title:
    def __init__(self):
        self.qn = 0
        self.ques = question(self)


# added LoginPage
def loginPage(logdata):
    signup_page.destroy()
    global login_page
    login_page = Tk()
    login_page.resizable(False, False)
    login_page.title('Conectare')

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login_page, width=720, height=440, bg="#B64D4D")
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="orange")
    login_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(login_frame, text="Conectare", fg="white", bg="orange")
    heading.config(font='calibri 40')
    heading.place(relx=0.34, rely=0.1)

    # USER NAME
    ulabel = Label(login_frame, text="Nume de utilizator", fg='white', bg='black')
    ulabel.place(relx=0.1, rely=0.4)
    uname = Entry(login_frame, bg='white', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.4)

    # PASSWORD
    plabel = Label(login_frame, text="Parola", fg='white', bg='black')
    plabel.place(relx=0.1, rely=0.5)
    passwd = Entry(login_frame, bg='white', fg='black', textvariable=password, show="*")
    passwd.config(width=42)
    passwd.place(relx=0.31, rely=0.5)

    def check():
        for a, b, c, d in logdata:
            if b == uname.get() and c == passwd.get():
                print(logdata)

                menu(a)
                break
        else:
            error = Label(login_frame, text="Nume de utilizator sau parola gresita!", fg='black', bg='white')
            error.place(relx=0.33, rely=0.7)

    # LOGIN BUTTON
    log = Button(login_frame, text='Conectare', padx=5, pady=5, width=5, command=check, fg="white", bg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.6)

    login_page.mainloop()


def signUpPage():
    window.destroy()
    global signup_page
    signup_page = Tk()
    signup_page.resizable(False, False)
    signup_page.title('Creare cont')

    fname = StringVar()
    uname = StringVar()
    passwd = StringVar()
    email = StringVar()

    sup_canvas = Canvas(signup_page, width=720, height=440, bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="#BADA55")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(sup_frame, text="Inregistrare", fg="#FFA500", bg="#BADA55")
    heading.config(font='calibri 40')
    heading.place(relx=0.3, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="Nume complet", fg='white', bg='black')
    flabel.place(relx=0.15, rely=0.4)
    fname = Entry(sup_frame, bg='white', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.31, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Nume utilizator", fg='white', bg='black')
    ulabel.place(relx=0.15, rely=0.5)
    uname = Entry(sup_frame, bg='white', fg='black', textvariable=uname)
    uname.config(width=42)
    uname.place(relx=0.31, rely=0.5)

    # password
    plabel = Label(sup_frame, text="Parola", fg='white', bg='black')
    plabel.place(relx=0.15, rely=0.6)
    pas = Entry(sup_frame, bg='white', fg='black', textvariable=passwd, show="*")
    pas.config(width=42)
    pas.place(relx=0.31, rely=0.6)

    # email
    elabel = Label(sup_frame, text="Email", fg='white', bg='black')
    elabel.place(relx=0.15, rely=0.7)
    email = Entry(sup_frame, bg='white', fg='black', textvariable=email)
    email.config(width=42)
    email.place(relx=0.31, rely=0.7)

    def addUserToDataBase():

        fname_added = fname.get()
        uname_added = uname.get()
        passwd_added = pas.get()
        email_added = email.get()

        if len(fname.get()) == 0 and len(uname.get()) == 0 and len(pas.get()) == 0 and len(email.get()) == 0:
            error = Label(text="Completati campurile de mai jos", fg='black', bg='red')
            error.place(relx=0.36, rely=0.15)

        elif len(fname.get()) == 0 or len(uname.get()) == 0 or len(pas.get()) == 0 or len(email.get()) == 0:
            error = Label(text="Completati campurile de mai jos", fg='black', bg='red')
            error.place(relx=0.36, rely=0.15)

        elif len(uname.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Numele de utilizator si parola incompletate", fg='black', bg='red')
            error.place(relx=0.36, rely=0.15)

        elif len(uname.get()) == 0 and len(pas.get()) != 0:
            error = Label(text="Nume de utilizator incomplet", fg='black', bg='red')
            error.place(relx=0.36, rely=0.15)

        elif len(uname.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Parola incompleta", fg='black', bg='red')
            error.place(relx=0.36, rely=0.15)

        else:

            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute(
                'CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,EMAIL text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",
                           (fname_added, uname_added, passwd_added, email_added))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            print(z)
            conn.close()
            loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # signup BUTTON
    sp = Button(sup_frame, text='Creare', padx=5, pady=5, width=5, command=addUserToDataBase, bg="black", fg="white")
    sp.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    sp.place(relx=0.4, rely=0.8)

    log = Button(sup_frame, text='Aveti deja un cont?', padx=5, pady=5, width=5, command=gotoLogin, bg="#BADA55",
                 fg="black")
    log.configure(width=16, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.393, rely=0.9)

    signup_page.mainloop()


def menu(name):
    login_page.destroy()
    global menu
    menu = Tk()
    menu.resizable(False, False)
    menu.title('Meniu')
    menu_canvas = Canvas(menu, width=800, height=600, bg="orange")
    menu_canvas.pack()

    wel = Label(menu_canvas, text=' Acesta este un test de cultura generala. ', fg="blue", bg="orange")
    wel.config(font='Broadway 22')
    wel.place(relx=0.15, rely=0.02)

    name = 'Bine ai venit ' + name
    level34 = Label(menu_canvas, text=name, bg="orange", font="calibri 18", fg="black")
    level34.place(relx=0.4, rely=0.15)  # 0.17 0.15
    img = ImageTk.PhotoImage(file="smile.png")
    menu_canvas.create_image(400, 300, anchor=tk.CENTER, image=img)

    def navigate():
        menu.destroy()
        last = tk.Tk()
        last.resizable(False, False)
        last.title('Chestionar de intrebari')

        last_canvas = Canvas(last, width=800, height=600, bg="SlateBlue2")
        last_canvas.pack()

        last_frame = Frame(last_canvas, bg="DarkSlateGray1")
        last_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        with open('quiz.json') as f:
            obj = json.load(f)
        quest = (obj['ques'])
        options = (obj['options'])
        answ = (obj['ans'])

        class Quiz:
            def __init__(self):
                self.opt_selected = IntVar()
                self.qn = 0
                self.ques = self.questions(self.qn)
                self.opts = self.radiobuttons()
                self.display_options(self.qn)
                self.buttons()
                self.correct = 0

            def questions(self, qn):
                t = Label(last_frame, text="Chestionar de intrebari", width=55, bg="DarkSlateGray1", fg="dark orange",
                          font="calibri 18")
                t.place(x=0, y=2)
                qn = Label(last_frame, text=quest[qn], width=50, font="calibri 16", anchor="w")
                qn.place(x=10, y=75)
                return qn

            def radiobuttons(self):
                val = 0
                blank_button = []
                yp = 150
                while val < 4:
                    button = Radiobutton(last_frame, text=" ", variable=self.opt_selected, value=val + 1,
                                      font=("times", 14))
                    blank_button.append(button)
                    button.place(x=100, y=yp)
                    val = val + 1
                    yp = yp + 40
                return blank_button

            def display_options(self, qn):
                val = 0
                self.opt_selected.set(0)
                self.ques['text'] = quest[qn]
                for op in options[qn]:
                    self.opts[val]['text'] = op
                    val = val + 1

            def buttons(self):
                next_button = Button(last_frame, text="Next", command=self.next_btn, bg="green", fg="white",
                                 font=("times", 16, "bold"))
                next_button.place(x=200, y=380)
                quit_button = Button(last_frame, text="Quit", width=10, bg="Red",
                                    fg="white", font=("times", 16, "bold"), command=last.destroy)
                quit_button.place(x=380, y=380)

            def checkans(self, qn):
                if self.opt_selected.get() == answ[qn]:
                    return True

            def next_btn(self):
                if self.checkans(self.qn):
                    self.correct += 1
                if self.qn < len(quest) - 1:
                    self.qn += 1
                    self.display_options(self.qn)
                else:
                    self.display_result()

            def display_result(self):
                score = int(self.correct / len(quest) * 100)
                result = "Ati obtinut un punctaj de: " + str(score) + "%"
                wc = len(quest) - self.correct
                correct = "Nr. de raspunsuri corecte este: " + str(self.correct)
                wrong = "Nr. de raspunsuri gresite este: " + str(wc)
                mb.showinfo("Rezultat", "\n".join([result, correct, wrong]))
                last.destroy()

        Quiz()
        last.mainloop()

    go_button = Button(menu_canvas, text="Sa incepem", bg="black", fg="white", font="calibri 16", command=navigate)
    go_button.place(relx=0.425, rely=0.8)
    menu.mainloop()


def main():
    canvas = tk.Canvas(window, width=800, height=520, bg='red')
    canvas.grid(column=0, row=1)
    img = tk.PhotoImage(file="prima3.png")
    canvas.create_image(400, 250, anchor=tk.CENTER, image=img)

    start_button = Button(window, text="Start test", bg="yellow", fg="black", command=signUpPage)
    start_button.configure(width=115, height=5, activebackground="#33B5E5", relief=RAISED)
    start_button.grid(column=0, row=2)

    Title()
    window.mainloop()


if __name__ == '__main__':
    main()
