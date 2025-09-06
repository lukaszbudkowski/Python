import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

from generator import generate_password
from password_strength import evaluate_strength
from storage import add_to_history, export_history

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Haseł")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # UI Elements
        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        self.password_var = tk.StringVar()
        self.strength_var = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        # Ustawienia
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Długość hasła:").pack(anchor="w")
        ttk.Spinbox(frame, from_=4, to=64, textvariable=self.length_var, width=5).pack(anchor="w")

        ttk.Checkbutton(frame, text="Wielkie litery", variable=self.upper_var).pack(anchor="w")
        ttk.Checkbutton(frame, text="Cyfry", variable=self.digits_var).pack(anchor="w")
        ttk.Checkbutton(frame, text="Symbole", variable=self.symbols_var).pack(anchor="w")

        ttk.Button(frame, text="Generuj hasło", command=self.generate).pack(pady=10)

        ttk.Entry(frame, textvariable=self.password_var, width=40, font=("Courier", 12)).pack()
        ttk.Label(frame, textvariable=self.strength_var, font=("Arial", 10, "bold")).pack(pady=5)

        # Przyciski
        btn_frame = ttk.Frame(frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text="Kopiuj", command=self.copy_password).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Eksportuj historię", command=self.export).pack(side="left", padx=5)

    def generate(self):
        try:
            pwd = generate_password(
                length=self.length_var.get(),
                use_upper=self.upper_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get()
            )
            self.password_var.set(pwd)
            strength = evaluate_strength(pwd)
            self.strength_var.set(f"Siła: {strength}")
            add_to_history(pwd)
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))

    def copy_password(self):
        pwd = self.password_var.get()
        if pwd:
            pyperclip.copy(pwd)
            messagebox.showinfo("Skopiowano", "Hasło zostało skopiowane do schowka.")

    def export(self):
        export_history()
        messagebox.showinfo("Eksport zakończony", "Historia została zapisana do pliku.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()
