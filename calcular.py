import sympy as sp


def calcular_basico():
    while True:
        print("\nCalculadora Básica en Python")
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz n-ésima")
        print("7. Salir")

        opcion = input("Ingrese el número de operación deseado (1/2/3/4/5/6/7): ")
        if opcion == '7':
            print("Saliendo de la calculadora básica.")
            break

        num1 = float(input("Ingrese el primer número: "))
        if opcion in ['1', '2', '3', '5']:
            num2 = float(input("Ingrese el segundo número: "))

        try:
            if opcion == '1':
                print("Resultado:", num1 + num2)
            elif opcion == '2':
                print("Resultado:", num1 - num2)
            elif opcion == '3':
                print("Resultado:", num1 * num2)
            elif opcion == '4':
                # Solicitamos el divisor solo si la opción es la división
                num2 = float(input("Ingrese el divisor (segundo número): "))
                print("Resultado:", num1 / num2)
            elif opcion == '5':
                print("Resultado:", num1 ** num2)
            elif opcion == '6':
                indice = float(input("Ingrese el índice de la raíz (ej. 2 para raíz cuadrada): "))
                print("Resultado:", num1 ** (1/indice))
        except ZeroDivisionError:
            print("No se puede dividir por 0.")
        except ValueError:
            print("Error en la entrada.")
        except Exception as e:
            print(f"Error: {e}")

            
def calcular_avanzado():

    print("Calculadora Avanzada en Python")
    print("Selecciona una operación:")
    print("1. Derivada")
    print("2. Integral")

    opcion = input("Ingrese el número de operación deseado (1/2/3): ")

    if opcion == '1':
        x = sp.symbols('x')
        funcion = input("Ingrese la función de la cual derivar (ejemplo: x**2): ")
        derivada = sp.diff(funcion, x)
        print(f"La derivada de {funcion} respecto a x es: {derivada}")
    elif opcion == '2':
        x = sp.symbols('x')
        funcion = input("Ingrese la función a integrar (ejemplo: x**2): ")
        integral = sp.integrate(funcion, x)
        print(f"La integral de {funcion} respecto a x es: {integral}")
    else:
        print("Opción inválida")
