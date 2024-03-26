import fuente
import calcular

# Imaginemos que "fuente" tiene una función para verificar si el archivo existe y procesarlo
resultado = fuente.procesar_y_predecir_imagen()
cal1 = calcular.calcular_basico()
cal1 = calcular.calcular_avanzado()

if resultado:
    print("Imagen procesada con éxito.")
    while True:  # Esto permitirá que el menú se repita hasta que el usuario decida salir.
        print("\nSeleccione el tipo de calculadora a usar o salir:")
        opcion = input("Escriba 'basico' para cálculos básicos, 'avanzado' para cálculos avanzados o 'salir' para terminar: ").lower()

        if opcion == 'basico':
            # Llama a la función de cálculo básico
            calcular.calcular_basico()
        elif opcion == 'avanzado':
            # Llama a la función de cálculo avanzado
            calcular.calcular_avanzado()
        elif opcion == 'salir':
            print("Saliendo del programa.")
            break  # Sale del bucle while y termina el programa.
        else:
            print("Opción no reconocida.")

    # Este input se mostrará solo después de que el usuario haya decidido salir del bucle.
    input("Presiona cualquier tecla para continuar...")

