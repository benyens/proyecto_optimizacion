% Parámetros básicos del problema
int: D;          % Número de días
int: B;          % Número de bloques por día
int: T;          % Total de bloques en la semana
int: num_salas;  % Número de salas disponibles
int: num_asignaturas; % Número de asignaturas a asignar
int: num_profesores;  % Número de profesores disponibles

% Parámetros relacionados con las asignaturas
array[1..num_asignaturas] of int: prioridad;        % Prioridad de cada asignatura
array[1..num_asignaturas] of int: bloques_necesarios; % Bloques necesarios por asignatura
array[1..num_asignaturas] of int: tipo_asignatura;  % 1 = indispensable, 0 = optativa
array[1..num_asignaturas] of int: profesor;         % Profesor asignado a cada asignatura

% Parámetros relacionados con las salas y estudiantes
array[1..num_salas] of int: capacidad_salas;        % Capacidad máxima de cada sala
array[1..num_asignaturas] of int: interes_curso;    % Interés de estudiantes por cada curso

% Parámetros de disponibilidad de los profesores
array[1..num_profesores, 1..T] of int: disponibilidad_profesor;  % 1 si el profesor está disponible en ese bloque

% Variables de decisión
array[1..num_salas, 1..T] of var 0..1: horario_salas;    % 1 si la sala está ocupada en un bloque
array[1..num_asignaturas] of var 1..num_salas: asignacion_sala; % Sala asignada a cada asignatura
array[1..num_asignaturas, 1..T] of var 0..1: asignacion_horario; % 1 si la asignatura se dicta en ese bloque

% Restricciones de bloques necesarios por asignatura
constraint forall(i in 1..num_asignaturas) (
    sum(t in 1..T)(asignacion_horario[i, t]) = bloques_necesarios[i]
);

% Restricción para asegurar que los bloques son consecutivos si la asignatura tiene 2 bloques
constraint forall(i in 1..num_asignaturas where bloques_necesarios[i] = 2) (
    exists(d in 0..D-1, b in 1..(B-1)) (
        asignacion_horario[i, d*B+b] = 1 /\ asignacion_horario[i, d*B+b+1] = 1
    )
);

% Asegurar que no haya conflictos de asignación de salas en el mismo horario
constraint forall(s in 1..num_salas, t in 1..T) (
    sum(i in 1..num_asignaturas)(asignacion_sala[i] = s /\ asignacion_horario[i, t] = 1) <= 1
);

% Asegurar que las asignaturas indispensables tengan salas asignadas
constraint forall(i in 1..num_asignaturas where tipo_asignatura[i] = 1)(
    sum(t in 1..T)(asignacion_horario[i, t]) = bloques_necesarios[i]
);

% Nueva restricción: asegurar que la capacidad de la sala asignada es suficiente para el interés del curso
constraint forall(i in 1..num_asignaturas)(
    interes_curso[i] <= capacidad_salas[asignacion_sala[i]]
);

% Restricción de disponibilidad de profesores: una asignatura solo puede dictarse en un bloque donde el profesor esté disponible
constraint forall(i in 1..num_asignaturas, t in 1..T) (
    asignacion_horario[i, t] = 1 -> disponibilidad_profesor[profesor[i], t] = 1
);

% Función objetivo: maximizar la suma de las prioridades de las asignaturas asignadas
var int: total_prioridad = sum(i in 1..num_asignaturas)(prioridad[i] * sum(t in 1..T)(asignacion_horario[i, t]));

solve maximize total_prioridad;
