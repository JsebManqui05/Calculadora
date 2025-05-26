# Función principal que realiza la operación matemática
def calcular(num1_str, num2_str, operacion):
    try:
        # Reemplaza comas por puntos para convertir correctamente a float
        num1 = float(num1_str.replace(",", "."))
        num2 = float(num2_str.replace(",", "."))

        # Estructura match para realizar la operación según el operador ingresado
        match operacion:
            case "+":
                return round(num1 + num2, 4)
            case "-":
                return round(num1 - num2, 4)
            case "*":
                return round(num1 * num2, 4)
            case "/":
                # Validación de división por cero
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                return round(num1 / num2, 4)
            case _:
                # Si se ingresa un operador inválido
                raise ValueError("Operación no válida.")
            
    # Propaga cualquier error para que la interfaz lo maneje
    except Exception as e:
        raise e
