
print(" SISTEMA DE REGISTRO DE CALIFICACIONES ")

ejecutando = True

while ejecutando:
    print("\n- REGISTRO DE NUEVO ESTUDIANTE -")

    # 1 Validacion de Nombre 
    mientras_nombre = True
    while mientras_nombre:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre != "":
            mientras_nombre = False
        else:
            print("ERROR: El nombre no puede estar vacío. Intente nuevamente.\n")

    # 2 Validacion de Calificación 1
    mientras_nota1 = True
    while mientras_nota1:
        try:
            nota1 = float(input("Ingrese la calificación 1 (0-100): "))
            if 0 <= nota1 <= 100:
                mientras_nota1 = False
            else:
                print("ERROR: La calificación debe estar entre 0 y 100. Ingrese nuevamente el dato.")
        except ValueError:
            print("ERROR: Entrada no válida. Debe ingresar un número entero o decimal.")

    # 3 Validación de Calificacion 2
    mientras_nota2 = True
    while mientras_nota2:
        try:
            nota2 = float(input("Ingrese la calificación 2 (0-100): "))
            if 0 <= nota2 <= 100:
                mientras_nota2 = False
            else:
                print("ERROR: La calificación debe estar entre 0 y 100. Ingrese nuevamente el dato.")
        except ValueError:
            print(">>> [DEPURACIÓN/FIX]: Se detectó texto o carácter no numérico. Intente nuevamente con un número válido.")

    # 4 Validación de Calificacion 3
    mientras_nota3 = True
    while mientras_nota3:
        try:
            nota3 = float(input("Ingrese la calificación 3 (0-100): "))
            if 0 <= nota3 <= 100:
                mientras_nota3 = False
            else:
                print("ERROR: La calificación debe estar entre 0 y 100. Ingrese nuevamente el dato.")
        except ValueError:
            print("ERROR: Entrada no válida. Debe ingresar un número entero o decimal.")

    # 5.  Estado
    promedio = (nota1 + nota2 + nota3) / 3.0
    
    if promedio >= 51:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    # 6 Mostrar Resultados
    print("      RESUMEN DE RENDIMIENTO       ")

    print(f" Estudiante : {nombre}")
    print(f" Notas      : {nota1}, {nota2}, {nota3}")
    print(f" Promedio   : {promedio:.2f}")
    print(f" Estado     : {estado}")
    print("====================================\n")

    # 7 Preguntar si se registra otro estudiante
    respuesta = input("¿Desea registrar otro estudiante? (s/n): ").strip().lower() #para evitar o anticiparnos a errores de sintaxis 
    if respuesta != "s":
        ejecutando = False
        print("\n¡Gracias por utilizar el sistema! Programa finalizado.")