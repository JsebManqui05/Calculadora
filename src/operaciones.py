def calcular(num1_str, num2_str, operacion):
    try:
        num1 = float(num1_str.replace(",", "."))
        num2 = float(num2_str.replace(",", "."))

        match operacion:
            case "+":
                return round(num1 + num2, 4)
            case "-":
                return round(num1 - num2, 4)
            case "*":
                return round(num1 * num2, 4)
            case "/":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                return round(num1 / num2, 4)
            case _:
                raise ValueError("Operación no válida.")
    except Exception as e:
        raise e
