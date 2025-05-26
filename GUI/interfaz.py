import customtkinter as ctk
from tkinter import messagebox
from src.operaciones import calcular

def lanzar_gui():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("Calculadora")
    app.geometry("400x350")

    def on_calcular():
        try:
            resultado = calcular(entry1.get(), entry2.get(), operacion.get())
            resultado_label.configure(text=f"Resultado: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ctk.CTkLabel(app, text="Calculadora", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)
    entry1 = ctk.CTkEntry(app, placeholder_text="Primer número")
    entry1.pack(pady=10)
    operacion = ctk.CTkComboBox(app, values=["+", "-", "*", "/"])
    operacion.set("+")
    operacion.pack(pady=10)
    entry2 = ctk.CTkEntry(app, placeholder_text="Segundo número")
    entry2.pack(pady=10)
    ctk.CTkButton(app, text="Calcular", command=on_calcular).pack(pady=20)
    resultado_label = ctk.CTkLabel(app, text="Resultado:", font=ctk.CTkFont(size=16))
    resultado_label.pack(pady=10)

    app.mainloop()


