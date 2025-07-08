import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game 🧠")
        self.root.geometry("400x300")

        self.level = tk.IntVar(value=5)
        self.sequence = []
        self.shuffled = []

        self.create_widgets()

    def create_widgets(self):
        # Etikett för instruktion
        self.label = tk.Label(self.root, text="Välj svårighetsgrad (antal tecken):")
        self.label.pack(pady=10)

        # Alternativ för svårighetsgrad
        self.level_option = tk.Spinbox(self.root, from_=3, to=10, textvariable=self.level)
        self.level_option.pack()

        # Startknapp
        self.start_btn = tk.Button(self.root, text="Starta spelet", command=self.start_game)
        self.start_btn.pack(pady=10)

        # Visning av sekvens
        self.display_label = tk.Label(self.root, font=("Helvetica", 16))
        self.display_label.pack(pady=10)

        # Inmatning från spelaren
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        # Knapp för att kontrollera gissning
        self.check_btn = tk.Button(self.root, text="Kontrollera gissning", command=self.check_guess)
        self.check_btn.pack(pady=10)

    def start_game(self):
        self.entry.delete(0, tk.END)
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.sequence = random.sample(chars, self.level.get())
        self.shuffled = self.sequence[:]
        random.shuffle(self.shuffled)

        self.display_label.config(text="Memorera: " + ' '.join(self.sequence))
        self.root.after(3000, self.show_shuffled)

    def show_shuffled(self):
        self.display_label.config(text="Blandad: " + ' '.join(self.shuffled))

    def check_guess(self):
        guess = self.entry.get().upper()
        if list(guess) == self.sequence:
            messagebox.showinfo("Rätt!", "Du klarade det! 🎉")
        else:
            messagebox.showerror("Fel", "Fel gissning. Försök igen!")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
