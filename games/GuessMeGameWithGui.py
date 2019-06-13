import random
from tkinter import *
from tkinter import messagebox

count_guess = 1
guessed = int(random.randint(1, 100))
MAX_GUESSED = 100


class Game:
    def __init__(self, count_guess, guessed):
        self.count_guess = count_guess
        self.guessed = guessed
        # GUI Window game
        self.root = Tk()
        self.frame = Frame(self.root).pack()
        self.root.wm_title("GUESS ME!")
        self.root.geometry("450x200")
        Label(self.root, text="WELCOME TO GUESS ME!", font="yellow").pack()
        Label(self.root, text="you need to guess number between 1 to 100", font="yellow").pack()
        Label(self.root, text="if your guess is too high, you get 'too high'", font="yellow").pack()
        Label(self.root, text="if your guess is too low, you get 'too low'", font="yellow").pack()
        Label(self.root, text="LEST GO!", font="yellow")

        self.entrytext = StringVar()
        self.entry = Entry(self.root, textvariable=self.entrytext)
        self.entry.pack()

        self.buttontext = StringVar()
        self.buttontext.set("Push Me!")
        self.button = Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.label = Label(self.root, text="")
        self.label.pack()

        self.root.mainloop()

    def new_game(self):
        self.entry.delete(0, 20)
        self.guessed = int(random.randint(1, 100))
        self.count_guess = 0
        self.label.configure(text="NEW GAME!", font='yellow')

    def clicked1(self):
        try:
            guess = int(self.entrytext.get())
            if guess == self.guessed:
                self.label.configure(text="CONGRATULATIONS, YOU GUESSED IT RIGHT!!", font='yellow')
                answer = messagebox.askquestion("Guess Me Game!", f"CONGRATULATIONS, YOU WIN after {self.count_guess} guesses!!!!!, do you want another game?")
                if answer.lower() == "yes":
                    self.new_game()
                else:
                    quit()
            elif guess > MAX_GUESSED:
                self.label.configure(text="your guess is to high!\n please try number between 1 to 100", font='yellow')
            elif guess > self.guessed:
                self.label.configure(text=f"your number: {guess} is Too High, please try again", font='yellow')
            else:
                self.label.configure(text=f"your number: {guess} is Too Low, please try again", font='yellow')
            self.count_guess += 1
        except ValueError:
            self.label.configure(text="you d'osnt insert a number!\n please try guess number between 1 to 100", font='yellow')


Game(count_guess, guessed)
