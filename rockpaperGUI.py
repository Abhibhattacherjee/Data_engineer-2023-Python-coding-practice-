import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.label = tk.Label(master, text="Rock, Paper, Scissors - shoot")
        self.label.pack()

        self.choices = ['Rock', 'Paper', 'Scissors']

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set(self.choices[0])  # default choice
        self.user_choice_menu = tk.OptionMenu(master, self.user_choice_var, *self.choices)
        self.user_choice_menu.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

    def play(self):
        user_choice = self.user_choice_var.get()
        opp_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, opp_choice)

        messagebox.showinfo("Result", result)

    def determine_winner(self, user_choice, opp_choice):
        if user_choice == opp_choice:
            return 'It\'s a Tie!'
        elif (user_choice == 'Rock' and opp_choice == 'Scissors') or \
             (user_choice == 'Paper' and opp_choice == 'Rock') or \
             (user_choice == 'Scissors' and opp_choice == 'Paper'):
            return f'You Win! {user_choice} beats {opp_choice}'
        else:
            return f'I Win! {opp_choice} beats {user_choice}'

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
