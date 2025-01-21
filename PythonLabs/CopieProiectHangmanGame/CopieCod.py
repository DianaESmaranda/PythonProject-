import tkinter as tk
from tkinter import messagebox
import random

# Funcție pentru a încărca cuvintele din fișier
def load_words():
    try:
        with open("words.txt", "r") as file:
            words = file.readlines()
        return [word.strip() for word in words if word.strip()]
    except FileNotFoundError:
        return []

# Clasa pentru logica jocului
class HangmanGame:
    def __init__(self):
        self.word_list = load_words()
        if not self.word_list:
            self.word_list = ["EXEMPLU", "PROGRAMARE", "PYTHON"]
        self.reset_game()

    def reset_game(self):
        self.word_to_guess = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_attempts = 6

# Clasa pentru interfața grafică
class HangmanApp:
    def __init__(self, root):
        self.game = HangmanGame()
        self.root = root
        self.root.title("Spânzurătoarea")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        # Încarcă imaginile pentru mesaje
        self.happy_image = tk.PhotoImage(file="happy.png")
        self.sad_image = tk.PhotoImage(file="sad.png")

        # Afișarea progresului cuvântului
        self.word_label = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 36), bg="lightblue")
        self.word_label.pack(pady=20)

        # Caseta de text pentru introducerea literelor
        self.letter_entry = tk.Entry(root, font=("Helvetica", 24))
        self.letter_entry.pack(pady=10)

        # Buton pentru ghicirea literei
        self.guess_button = tk.Button(root, text="Ghiceste", font=("Helvetica", 18), command=self.guess_letter)
        self.guess_button.pack(pady=10)

        # Etichetă pentru afișarea greșelilor
        self.wrong_label = tk.Label(root, text=f"Greșeli: {self.game.wrong_guesses}/{self.game.max_attempts}", font=("Helvetica", 18), fg="red", bg="pink")
        self.wrong_label.pack(pady=10)

        # Etichetă pentru a arăta omul care se formează
        self.man_label = tk.Label(root, text=self.get_hangman_image(), font=("Courier", 24), bg="lightblue")
        self.man_label.pack(pady=20)

        # Buton pentru resetarea jocului
        self.reset_button = tk.Button(root, text="Resetează jocul", font=("Helvetica", 18), command=self.reset_game)
        self.reset_button.pack(pady=10)

    # Afișează cuvântul cu litere ghicite și „_” pentru cele negicite
    def get_display_word(self):
        return " ".join([letter if letter in self.game.guessed_letters else "_" for letter in self.game.word_to_guess])

    # Afișează omul în funcție de numărul de greșeli
    def get_hangman_image(self):
        stages = [
            "",  # 0 greșeli
            "O",  # 1 greșeală - cap
            "O\n|",  # 2 greșeli - corp
            "O\n/|",  # 3 greșeli - brațe
            "O\n/|\\",  # 4 greșeli - brațe complete
            "O\n/|\\\n  /",  # 5 greșeli - picior stâng
            "O\n/|\\\n/ \\ ",  # 6 greșeli - omuleț complet
        ]
        return stages[self.game.wrong_guesses]

    # Logica pentru ghicirea unei litere
    def guess_letter(self):
        letter = self.letter_entry.get().strip().upper()
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Eroare", "Introdu o literă validă!")
            return

        if letter in self.game.guessed_letters:
            messagebox.showinfo("Info", "Această literă a fost deja ghicită!")
            return

        self.game.guessed_letters.add(letter)
        if letter in self.game.word_to_guess:
            self.word_label.config(text=self.get_display_word())
            if set(self.game.word_to_guess) <= self.game.guessed_letters:
                # Câștig
                self.display_end_game_message("Ai câștigat!", self.happy_image)
        else:
            self.game.wrong_guesses += 1
            self.wrong_label.config(text=f"Greșeli: {self.game.wrong_guesses}/{self.game.max_attempts}")
            self.man_label.config(text=self.get_hangman_image())  # Actualizează omulețul
            if self.game.wrong_guesses >= self.game.max_attempts:
                # Pierdere
                self.display_end_game_message(f"Ai pierdut! Cuvântul era {self.game.word_to_guess}", self.sad_image)

        self.letter_entry.delete(0, tk.END)

    def display_end_game_message(self, message, image):
        # Creează o fereastră de mesaj personalizată
        end_game_window = tk.Toplevel(self.root)
        end_game_window.title("Finalul jocului")
        end_game_window.geometry("500x700")
        end_game_window.resizable(False, False)

        # Mesajul text
        message_label = tk.Label(end_game_window, text=message, font=("Helvetica", 16), fg="green")
        message_label.pack(pady=25)

        # Afișarea imaginii
        image_label = tk.Label(end_game_window, image=image)
        image_label.image = image  # Salvează referința imaginii
        image_label.pack(pady=25)

        # Butonul OK
        ok_button = tk.Button(end_game_window, text="OK", font=("Helvetica", 14), command=end_game_window.destroy, bg="lightgreen", activebackground="darkgreen")
        ok_button.pack(pady=25)

    # Resetarea jocului
    def reset_game(self):
        self.game.reset_game()
        self.word_label.config(text=self.get_display_word())
        self.wrong_label.config(text=f"Greșeli: {self.game.wrong_guesses}/{self.game.max_attempts}")
        self.man_label.config(text=self.get_hangman_image())  # Resetăm omul
        self.letter_entry.delete(0, tk.END)

# Inițierea aplicației
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
