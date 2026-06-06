
STOCK_MAXIMO = 120
stock_disponible = 120
historial_prestamos = 0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

# Menú principal
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    # Validar opción
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Opción inválida. Por favor ingresa un número entero del 1 al 5.")
        continue

    # Opción 1: Libros disponibles
    if opcion == 1:
        print(f"Libros disponibles actualmente: {stock_disponible} de {STOCK_MAXIMO}")

    # Opción 2: Realizar préstamo
    elif opcion == 2:
        if stock_disponible == 0:
            print("No hay libros disponibles para préstamo en este momento.")
        else:
            while True:
                try:
                    cantidad_prestar = int(
                        input(f"¿Cuántos libros desea prestar? (disponibles: {stock_disponible}): ")
                    )

                    if cantidad_prestar <= 0:
                        print("La cantidad a solicitar debe ser mayor a 0.")

                    elif cantidad_prestar > stock_disponible:
                        print(f"No hay suficientes libros. Máximo disponible: {stock_disponible}.")

                    else:
                        stock_disponible -= cantidad_prestar
                        historial_prestamos += cantidad_prestar
                        print(f"Préstamo exitoso. Se prestaron {cantidad_prestar} libro(s).")
                        break

                except ValueError:
                    print("¡Error de datos! Ingresa un número entero válido para la cantidad.")

    # Opción 3: Devolver préstamo
    elif opcion == 3:
        if stock_disponible == STOCK_MAXIMO:
            print("Todos los libros están en la biblioteca. No hay inventario por devolver.")
        else:
            while True:
                try:
                    cantidad_devolver = int(input("¿Cuántos libros desea devolver?: "))

                    if cantidad_devolver <= 0:
                        print("La cantidad a devolver debe ser mayor a 0.")

                    elif stock_disponible + cantidad_devolver > STOCK_MAXIMO:
                        print(
                            f"Error. Excede el límite de la biblioteca. "
                            f"Solo puedes devolver hasta {STOCK_MAXIMO - stock_disponible} libro(s)."
                        )

                    else:
                        stock_disponible += cantidad_devolver
                        historial_prestamos -= cantidad_devolver
                        print(f"Devolución exitosa. Se recibieron {cantidad_devolver} libro(s).")
                        break

                except ValueError:
                    print("¡Error de datos! Ingresa un número entero válido para la devolución.")

    # Opción 4: Historial de préstamos
    elif opcion == 4:
        print(f"Total de préstamos activos durante la sesión: {historial_prestamos}")

    # Opción 5: Salir
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    # Opción fuera de rango
    else:
        print("Opción no válida. Por favor selecciona un número entre 1 y 5.")
