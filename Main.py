import fuente

# Imaginemos que "fuente" tiene una función para verificar si el archivo existe y procesarlo
resultado = fuente.procesar_y_predecir_imagen()

if resultado:
    def calcular():
        print("Calculadora Simple en Python")
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        
        opcion = input("Ingrese el número de operación deseado (1/2/3/4): ")
        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", num1 + num2)
        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", num1 - num2)
        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("Resultado:", num1 * num2)
        elif opcion == '4':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Opción inválida")

    calcular()
