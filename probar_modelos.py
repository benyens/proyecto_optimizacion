import minizinc
import os

def ejecutar_modelo(model_file, data_file):
    # Crear el modelo MiniZinc
    model = minizinc.Model(model_file)  # Cargar el modelo .mzn
    model.add_file(data_file)           # Agregar el archivo .dzn

    # Crear el solver (puedes usar otro solver como `chuffed` o `coin-bc`)
    solver = minizinc.Solver.lookup("coin-bc")

    # Crear la instancia con el modelo y el solver
    instance = minizinc.Instance(solver, model)

    # Ejecutar el modelo con los datos y obtener el resultado
    result = instance.solve()

    # Imprimir el resultado
    print(f"Resultado de la ejecución para '{data_file}':")
    print(result)
    with open("resultados.txt", "w") as f:
        f.write(str(result))
    return result

# Archivo del modelo .mzn
model_file = "modeloxd.mzn"

# Instancias de prueba generadas por el script
data_files = [
    "instancia_mediana_A1B2.dzn",  # Ajustar los nombres a las instancias generadas
    "instancia_grande_A1B2.dzn"
]

# Probar cada instancia generada
for data_file in data_files:
    if os.path.exists(data_file):
        print(f"Ejecutando el modelo con la instancia '{data_file}'")
        ejecutar_modelo(model_file, data_file)
    else:
        print(f"El archivo de datos '{data_file}' no existe.")