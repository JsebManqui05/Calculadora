# Ingresar los números
numero_1_str = input("Ingrese el primer número: ")
operacion = input("Ingrese la operación (+, -, *, /): ")
numero_2_str = input("Ingrese el segundo número: ")

# Conversión robusta
try:
    numero_1 = float(numero_1_str.replace(",", "."))
    numero_2 = float(numero_2_str.replace(",", "."))

    # Operación
    match operacion:
        case "+":
            res = numero_1 + numero_2
        case "-":
            res = numero_1 - numero_2
        case "*":
            res = numero_1 * numero_2
        case "/":
            if numero_2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            res = numero_1 / numero_2
        case _:
            raise ValueError("Operación no válida.")

    print(f"El resultado de {numero_1} {operacion} {numero_2} es: {res}")

except ValueError:
    print("Por favor, ingrese números válidos y una operación correcta.")
except ZeroDivisionError as zde:
    print("Error:", zde)
except Exception as e:
    print("Error inesperado:", e)