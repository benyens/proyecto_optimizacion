
```markdown
# Proyecto de Optimización - Grupo 6

Este repositorio contiene el proyecto de optimización desarrollado por el Grupo 6. El objetivo de este proyecto es asignar asignaturas a salas y bloques horarios en base a diferentes restricciones y maximizar la prioridad total de las asignaturas asignadas.

## Estructura del Proyecto

- **`modeloxd.mzn`**: El modelo de MiniZinc que define el problema de optimización. Este archivo incluye las variables de decisión, las restricciones y la función objetivo a maximizar.
- **`generador_instancias.py`**: Script en Python para generar instancias del problema de asignación. Se puede elegir entre generar una instancia de tipo "mediana" o "grande".
- **`probar_modelos.py`**: Script en Python para ejecutar y probar los modelos generados en `modeloxd.mzn` con las instancias generadas en `.dzn`.

## Archivos

1. **`modeloxd.mzn`**: 
   - Este archivo contiene el modelo de optimización utilizando MiniZinc.
   - El objetivo es maximizar la prioridad total de las asignaturas asignadas a las salas.
   - Se consideran restricciones como la asignación de bloques requeridos, la disponibilidad de los profesores, y la restricción de no asignar más de una asignatura en la misma sala y bloque.

2. **`generador_instancias.py`**: 
   - Genera instancias aleatorias del problema según los parámetros de tipo "mediana" o "grande".
   - Las prioridades de las asignaturas, los bloques necesarios y la disponibilidad de los profesores se generan de manera aleatoria.
   - Guarda las instancias en archivos `.dzn` que pueden ser leídos por el modelo en MiniZinc.

3. **`probar_modelos.py`**: 
   - Script para ejecutar las instancias generadas con el modelo MiniZinc. 
   - Se pueden modificar los parámetros para probar diferentes instancias o modelos.

## Ejecución

### Generar Instancias

Para generar una instancia del problema, puedes utilizar el archivo `generador_instancias.py`. Aquí un ejemplo de cómo ejecutar el generador para una instancia de tipo "mediana":

```bash
python generador_instancias.py
```

Esto generará un archivo `.dzn` con los datos de la instancia, que luego puede ser utilizado con el modelo de MiniZinc.

### Ejecutar el Modelo

Una vez generadas las instancias, puedes ejecutar el modelo utilizando MiniZinc. Desde la línea de comandos:

```bash
minizinc modeloxd.mzn instancia_mediana.dzn
```

Este comando ejecutará el modelo en MiniZinc y resolverá el problema de asignación con los datos de la instancia.

