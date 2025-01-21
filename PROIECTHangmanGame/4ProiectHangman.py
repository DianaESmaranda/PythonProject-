import tkinter as tk
import random
import speech_recognition as sr
from tkinter import messagebox
from PIL import Image, ImageTk

# Lista de cuvinte pentru jocul de Spânzurătoarea
words = ["programare", "python", "inteligenta", "calculator", "algoritm", "baza"]


class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spânzurătoarea")
        self.root.geometry("400x500")

        # Inițializare joc
        self.start_game()

        # Crearea interfeței grafice
        self.word_label = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 20))
        self.word_label.pack(pady=20)

        self.attempts_label = tk.Label(root, text=f"Încercări rămase: {self.attempts_left}", font=("Helvetica", 14))
        self.attempts_label.pack(pady=10)

        self.letter_entry = tk.Entry(root, font=("Helvetica", 18))
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Ghicește litera", font=("Helvetica", 18), command=self.guess_letter)
        self.guess_button.pack(pady=10)

        # Buton pentru ghicirea vocală a literei
        self.voice_button = tk.Button(root, text="Ghiceste vocal", font=("Helvetica", 18), command=self.voice_guess)
        self.voice_button.pack(pady=10)

        # Buton de restart joc
        self.restart_button = tk.Button(root, text="Restart joc", font=("Helvetica", 18), command=self.restart_game)
        self.restart_button.pack(pady=10)

        # Etichetă pentru reprezentarea omulețului
        self.hangman_label = tk.Label(root, text=self.get_hangman_image(), font=("Courier", 16))
        self.hangman_label.pack(pady=20)

        # Eticheta pentru litera ghicită vocal
        self.voice_guess_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.voice_guess_label.pack(pady=10)

    def start_game(self):
        # Alegerea cuvântului la întâmplare
        self.word = random.choice(words).lower()
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def get_display_word(self):
        # Afișează cuvântul cu literele ghicite și _ pentru literele neghicite
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def get_hangman_image(self):
        # Reprezentarea textuală a omulețului
        stages = [
            "",  # 0 greșeli
            "O",  # 1 greșeală - cap
            "O\n|",  # 2 greșeli - corp
            "O\n/|",  # 3 greșeli - brațe
            "O\n/|\\",  # 4 greșeală - brațe complete
            "O\n/|\\\n/",  # 5 greșeală - picior stâng
            "O\n/|\\\n/ \\",  # 6 greșeală - omuleț complet
        ]
        return stages[self.max_attempts - self.attempts_left]

    def guess_letter(self):
        # Ghicește litera introdusă de utilizator
        letter = self.letter_entry.get().lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in self.guessed_letters:
                messagebox.showwarning("Avertisment", "Litera încercată deja!")
            else:
                self.guessed_letters.append(letter)
                if letter not in self.word:
                    self.attempts_left -= 1
        else:
            messagebox.showwarning("Avertisment", "Te rog introdu o literă validă!")

        # Actualizează afișajul
        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text=f"Încercări rămase: {self.attempts_left}")
        self.hangman_label.config(text=self.get_hangman_image())

        # Verifică dacă jocul s-a terminat
        if self.attempts_left == 0:
            self.show_game_over("Ai pierdut! Cuvântul era: " + self.word, "sad.png")
        elif "_" not in self.get_display_word():
            self.show_game_over("Felicitări! Ai ghicit cuvântul.", "happy.png")

        self.letter_entry.delete(0, tk.END)

    def show_game_over(self, message, image_path):
        # Afișează mesajul de final al jocului și imaginea corespunzătoare
        self.game_over_window = tk.Toplevel(self.root)
        self.game_over_window.title("Finalul jocului")

        # Adăugarea imaginii
        img = Image.open(image_path)
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(self.game_over_window, image=img_tk)
        img_label.image = img_tk
        img_label.pack(pady=20)

        # Mesajul
        message_label = tk.Label(self.game_over_window, text=message, font=("Helvetica", 16))
        message_label.pack(pady=10)

        # Butonul de restart
        restart_button = tk.Button(self.game_over_window, text="Restart joc", font=("Helvetica", 14),
                                   command=self.restart_game)
        restart_button.pack(pady=10)

    def restart_game(self):
        # Resetează jocul și închide fereastra de final
        if hasattr(self, 'game_over_window'):
            self.game_over_window.destroy()

        self.start_game()

        # Actualizează interfața
        self.word_label.config(text=self.get_display_word())
        self.attempts_label.config(text=f"Încercări rămase: {self.attempts_left}")
        self.hangman_label.config(text=self.get_hangman_image())

        # Activează butoanele
        self.guess_button.config(state=tk.NORMAL)
        self.voice_button.config(state=tk.NORMAL)

    def voice_guess(self):
        # Folosește recunoașterea vocală pentru a ghici o literă
        self.voice_guess_label.config(text="Ascult... Spune o literă.")
        self.root.update()
        letter = listen_for_letter()
        if letter:
            self.letter_entry.delete(0, tk.END)
            self.letter_entry.insert(0, letter)
            self.guess_letter()
            self.voice_guess_label.config(text=f"Litera ghicită vocal: {letter}")
        else:
            self.voice_guess_label.config(text="Nu s-a recunoscut o literă validă. Încearcă din nou.")


def listen_for_letter():
    # Funcția pentru recunoașterea vocală
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("Ascult... Spune o literă.")
            audio = recognizer.listen(source, timeout=5)

            letter = recognizer.recognize_google(audio, language="ro-RO").strip().lower()
            if len(letter) == 1 and letter.isalpha():
                return letter
            else:
                print("Nu s-a recunoscut o literă validă.")
                return None
        except sr.UnknownValueError:
            print("Nu am înțeles ce ai spus. Încearcă din nou.")
        except sr.RequestError as e:
            print(f"Eroare de rețea: {e}")
        except sr.WaitTimeoutError:
            print("Nu ai spus nimic în timpul alocat.")
    return None


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
