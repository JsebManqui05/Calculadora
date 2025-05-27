import customtkinter as ctk
from tkinter import messagebox
from src.operaciones import calcular  # Lógica de cálculo


def lanzar_gui():
    # Apariencia
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("Calculadora")
    app.geometry("400x400")

    # Variable para guardar la operación seleccionada
    operacion_actual = {"valor": "+"}

    # Función para actualizar la operación al hacer clic en un botón
    def seleccionar_operacion(op):
        operacion_actual["valor"] = op
        operacion_label.configure(text=f"Operación seleccionada: {op}")

    # Función que se ejecuta al presionar "="
    def on_calcular():
        try:
            resultado = calcular(entry1.get(), entry2.get(), operacion_actual["valor"])
            resultado_label.configure(text=f"Resultado: {resultado}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Título
    ctk.CTkLabel(app, text="Calculadora", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)

    # Primer número
    entry1 = ctk.CTkEntry(app, placeholder_text="Primer número")
    entry1.pack(pady=10)

    # frame para los botones de operación
    frame_botones = ctk.CTkFrame(app)
    frame_botones.pack(pady=10)

    # Crear botones de operación y asociarlos con la función de selección
    for simbolo in ["+", "-", "*", "/"]:
        ctk.CTkButton(frame_botones, text=simbolo, width=50, command=lambda op=simbolo: seleccionar_operacion(op)).pack(side="left", padx=5)

    # Etiqueta que muestra la operación actual
    operacion_label = ctk.CTkLabel(app, text="Operación seleccionada: +", font=ctk.CTkFont(size=14))
    operacion_label.pack(pady=5)

    # Segundo número
    entry2 = ctk.CTkEntry(app, placeholder_text="Segundo número")
    entry2.pack(pady=10)

    # Botón igual "=" para ejecutar el calculo
    ctk.CTkButton(app, text="=", command=on_calcular, width=100, height=40, font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

    # Resultado
    resultado_label = ctk.CTkLabel(app, text="Resultado:", font=ctk.CTkFont(size=16))
    resultado_label.pack(pady=10)

    # Lanza el bucle principal de la aplicación
    app.mainloop()


