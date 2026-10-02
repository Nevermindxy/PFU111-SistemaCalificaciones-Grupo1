print("=== SISTEMA DE REGISTRO DE CALIFICACIONES ===")

nombre = input("Ingrese el nombre del estudiante: ")
nota1 = float(input("Ingrese la calificación 1: "))
nota2 = float(input("Ingrese la calificación 2: "))
nota3 = float(input("Ingrese la calificación 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 51:
    estado = "Aprobado"
else:
    estado = "Reprobado"

print("\n--- RESULTADO ---")
print(f"Estudiante: {nombre}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}\n")