def main():
    print("Bienvenido al registro de estudiantes")


if __name__ == "__main__":
    main()
#Crear un programa que perimita registrar la nota de los alumnos y al final muestre un resumen de los resultados
# GESTOR DE CALIFICACIONES EN PYTHON

print(" REGISTRO DE ESTUDIANTES DE TECNOLOGICO ARGOS")

# Ingreso y validación de cantidad de estudiantes
while True:
    try: 
        num_estudiantes = int(input("\n¿Cuántos alumnos hay en la clase?: "))
        if num_estudiantes > 0:
            break
        else:
            print("ERROR: Ingrese un número mayor que cero.")
    except ValueError:
        print("ERROR: Ingrese un número válido.")

# Listas para almacenar nombres y notas
nombres = []
notas = []

aprobados = 0
reprobados = 0

# Registro de los estudiantes
for i in range(num_estudiantes):
    nombre = input(f"\n[Estudiante #{i + 1}] Ingrese el nombre: ").strip()

    # Validar la nota
    while True:
        try:
            nota = float(input(f"[Estudiante #{i + 1}] Ingrese la nota (0 - 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("ERROR: Ingrese una nota válida entre 0 y 10")  
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    nombres.append(nombre)
    notas.append(nota)

    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1

# Cálculos de estadísticas
promedio = sum(notas) / len(notas)
nota_max = max(notas)

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"Total estudiantes: {num_estudiantes}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Promedio general: {promedio:.2f}")


input("\nPresione ENTER para finalizar...")