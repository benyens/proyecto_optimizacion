import random

def generar_instancia_A1B2(instancia, num_asignaturas, num_salas, num_profesores, dzn_file_name):
    """
    Genera instancias para A = 1 (Capacidad de salas 20-45, interés de alumnos 10-40)
    y B = 2 (65% de las asignaturas tienen 2 bloques por semana, el resto tiene 1 bloque).
    :param instancia: Nombre de la instancia (por ejemplo, "mediana" o "grande").
    :param num_asignaturas: Número de asignaturas en la instancia.
    :param num_salas: Número de salas disponibles.
    :param num_profesores: Número de profesores disponibles.
    :param dzn_file_name: Nombre del archivo .dzn a generar.
    """
    D = 5   # Días de la semana (lunes a viernes)
    B_TOTAL = 7   # Bloques por día
    T = D * B_TOTAL  # Total de bloques en la semana

    print(f"Generando instancia {instancia} con {num_asignaturas} asignaturas, {num_salas} salas y {num_profesores} profesores.")

    # 1. Definir las características de las asignaturas
    prioridad = []
    bloques_necesarios = []
    tipo_asignatura = []
    profesor = []
    interes_curso = []  #

    # Capacidad de las salas y tamaño del curso según A = 1
    capacidad_salas = [random.randint(20, 45) for _ in range(num_salas)]
    interes_min, interes_max = 10, 40  # Tamaño de los cursos para A = 1

    # Proporción de asignaturas con 2 bloques (65%) y 1 bloque (35%)
    distribucion_bloques = 0.65

    # Generar las asignaturas con las características dadas
    for i in range(num_asignaturas):
        if i < num_asignaturas // 5:  # Un 20% de las asignaturas son indispensables
            prioridad.append(random.randint(6, 10))  # Prioridad para asignaturas indispensables
            tipo_asignatura.append(1)  # Asignatura indispensable
        else:
            prioridad.append(random.randint(1, 5))  # Prioridad para asignaturas optativas
            tipo_asignatura.append(0)  # Asignatura optativa

        # Asignar bloques de acuerdo a la distribución indicada
        if random.random() < distribucion_bloques:  # 65% de las asignaturas tienen 2 bloques por semana
            bloques_necesarios.append(2)
        else:
            bloques_necesarios.append(1)

        # Asignar un profesor aleatorio para cada asignatura
        profesor.append(random.randint(1, num_profesores))

        # Generar el interés (tamaño del curso)
        interes_curso.append(random.randint(interes_min, interes_max))

    print("Características de las asignaturas generadas correctamente.")

    # 2. Definir la disponibilidad de los profesores
    disponibilidad_profesor = []
    for p in range(num_profesores):
        disponibilidad = [0] * T
        num_disponible = random.randint(14, 28)  # Cada profesor disponible en un rango de 14 a 28 bloques
        bloques_disponibles = random.sample(range(T), num_disponible)  # Elegir bloques disponibles aleatoriamente
        for bloque in bloques_disponibles:
            disponibilidad[bloque] = 1
        disponibilidad_profesor.append(disponibilidad)

    print("Disponibilidad de los profesores generada correctamente.")

    # 3. Escribir la instancia en un archivo .dzn
    with open(dzn_file_name, 'w') as f:
        f.write(f"D = {D};\n")
        f.write(f"B = {B_TOTAL};\n")
        f.write(f"T = {T};\n") 
        f.write(f"num_salas = {num_salas};\n")
        f.write(f"num_asignaturas = {num_asignaturas};\n")
        f.write(f"num_profesores = {num_profesores};\n")

        f.write(f"prioridad = [{', '.join(map(str, prioridad))}];\n")
        f.write(f"bloques_necesarios = [{', '.join(map(str, bloques_necesarios))}];\n")
        f.write(f"tipo_asignatura = [{', '.join(map(str, tipo_asignatura))}];\n")
        f.write(f"profesor = [{', '.join(map(str, profesor))}];\n")
        f.write(f"interes_curso = [{', '.join(map(str, interes_curso))}];\n")
        f.write("disponibilidad_profesor = array2d(1..num_profesores, 1..T, [")
        for i, disp in enumerate(disponibilidad_profesor):
            if i > 0:
                f.write(", ")
            f.write(", ".join(map(str, disp)))
        f.write("]);\n")
        f.write(f"capacidad_salas = [{', '.join(map(str, capacidad_salas))}];\n")

    print(f"Instancia '{dzn_file_name}' generada con éxito!")

# Generar instancias para A = 1 y B = 2
generar_instancia_A1B2("mediana", num_asignaturas=45, num_salas=4, num_profesores=15, dzn_file_name="instancia_mediana_A1B2.dzn")
generar_instancia_A1B2("grande", num_asignaturas=200, num_salas=11, num_profesores=30, dzn_file_name="instancia_grande_A1B2.dzn")
