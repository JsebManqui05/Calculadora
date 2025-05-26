# Importa el módulo CustomTkinter y messagebox de tkinter
import customtkinter as ctk
from tkinter import messagebox
# Importa la función calcular desde src/operaciones.py
from src.operaciones import calcular # Importa la lógica de cálculo

# Función que lanza la interfaz gráfica
def lanzar_gui():
    # Modo visual: puede ser "Light", "Dark" o seguir la configuración del sistema
    ctk.set_appearance_mode("System")
        
    # Establece el color principal del tema: "green", "blue", "dark-blue"
    ctk.set_default_color_theme("green")

    # Crea la ventana principal de la aplicación
    app = ctk.CTk()
    app.title("Calculadora") # Título de la ventana
    app.geometry("400x350") # Tamaño inicial (ancho x alto)

    # Función que se ejecuta al presionar "Calcular"
    def on_calcular():
        try:
            # Toma los valores ingresados y ejecuta la lógica
            resultado = calcular(entry1.get(), entry2.get(), operacion.get())

            # Muestra el resultado en la etiqueta
            resultado_label.configure(text=f"Resultado: {resultado}")

        # Si ocurre un error (como dividir por cero), muestra una alerta
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Título en la parte superior
    ctk.CTkLabel(app, text="Calculadora", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)

    # Primer campo de entrada
    entry1 = ctk.CTkEntry(app, placeholder_text="Primer número")
    entry1.pack(pady=10)

    # Menú desplegable para elegir la operación (+, -, *, /)
    operacion = ctk.CTkComboBox(app, values=["+", "-", "*", "/"])
    operacion.set("+")
    operacion.pack(pady=10)

    # Segundo campo de entrada
    entry2 = ctk.CTkEntry(app, placeholder_text="Segundo número")
    entry2.pack(pady=10)

    # Botón que ejecuta el cálculo
    ctk.CTkButton(app, text="Calcular", command=on_calcular).pack(pady=20)

    # Etiqueta donde se mostrará el resultado
    resultado_label = ctk.CTkLabel(app, text="Resultado:", font=ctk.CTkFont(size=16))
    resultado_label.pack(pady=10)

    # Lanza el bucle principal de la aplicación
    app.mainloop()


