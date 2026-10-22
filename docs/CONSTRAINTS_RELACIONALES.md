# Documentación de Constraints Relacionales - SIPAM

## Llaves Foráneas (Foreign Keys)

### Modelo User
- Sin FK directas (es la entidad base)

### Modelo Convocatoria
- `asignatura_id` → ForeignKey("asignaturas.id")
- `profesor_id` → ForeignKey("users.id")

### Modelo Asignatura
- `profesor_id` → ForeignKey("users.id")

### Modelo Postulacion
- `convocatoria_id` → ForeignKey("convocatorias.id")
- `estudiante_id` → ForeignKey("users.id")

### Modelo ArchivoAdjunto
- `postulacion_id` → ForeignKey("postulaciones.id")
- `usuario_id` → ForeignKey("users.id")

### Modelo AsignaturaEstudiante
- `asignatura_id` → ForeignKey("asignaturas.id")
- `estudiante_id` → ForeignKey("users.id")

### Modelo MonitoriaPlantilla
- `asignatura_id` → ForeignKey("asignaturas.id")

## Restricciones de Unicidad (Unique Constraints)

### User
- `codigo` - unique=True
- `email` - unique=True
- `cedula` - unique=True

### Asignatura
- `codigo` - unique=True

### ArchivoAdjunto
- `nombre_almacenado` - unique=True

### UniqueConstraints (Multi-columna)
- **Convocatoria**: `(asignatura_id, periodo_academico)` - Una convocatoria única por asignatura y periodo
- **Postulacion**: `(convocatoria_id, estudiante_id)` - Un estudiante solo puede postular una vez a una convocatoria
- **AsignaturaEstudiante**: `(asignatura_id, estudiante_id, periodo_academico)` - Una matrícula única por estudiante, asignatura y periodo

## Restricciones de No Nulidad (nullable=False)

### User
- codigo, nombres, apellidos, email, cedula, hashed_password, rol

### Convocatoria
- titulo, asignatura_id, profesor_id, periodo_academico, fecha_inicio_postulacion, fecha_fin_postulacion, horas_semana, horas_semestre

### Asignatura
- codigo, nombre, creditos, programa, semestre

### Postulacion
- convocatoria_id, estudiante_id, estado

### ArchivoAdjunto
- usuario_id, tipo_documento, nombre_original, nombre_almacenado, ruta_archivo

## Check Constraints (Validaciones de Dominio)

### User
- `promedio >= 0 AND promedio <= 5`
- `porcentaje_creditos >= 0 AND porcentaje_creditos <= 100`

### Convocatoria
- `promedio_minimo >= 0 AND promedio_minimo <= 5`
- `horas_semana > 0`
- `horas_semestre > 0`
- `num_monitores_requeridos > 0`

### Asignatura
- `creditos > 0`
- `semestre >= 1 AND semestre <= 12`

### Postulacion
- `nota_asignatura >= 0 AND nota_asignatura <= 5`
- `nota_entrevista >= 0 AND nota_entrevista <= 5`
- `promedio_estudiante >= 0 AND promedio_estudiante <= 5`

## Índices (Indexes)

### User
- ix_users_codigo (codigo)
- ix_users_email (email)
- ix_users_rol (rol)
- ix_users_programa (programa)
- ix_users_sede (sede)

### Convocatoria
- ix_convocatorias_estado (estado)
- ix_convocatorias_periodo (periodo_academico)
- ix_convocatorias_profesor (profesor_id)

### Asignatura
- ix_asignaturas_codigo (codigo)
- ix_asignaturas_programa (programa)
- ix_asignaturas_profesor (profesor_id)

### Postulacion
- ix_postulaciones_convocatoria_estado (convocatoria_id, estado)
- ix_postulaciones_estudiante (estudiante_id)

## Relaciones ORM (Relationships)

### User
- `postulaciones` → Postulacion (back_populates="estudiante")
- `archivos` → ArchivoAdjunto (back_populates="usuario")

### Convocatoria
- `asignatura` → Asignatura (back_populates="convocatorias")
- `profesor` → User
- `postulaciones` → Postulacion (back_populates="convocatoria", cascade="all, delete-orphan")

### Asignatura
- `convocatorias` → Convocatoria (back_populates="asignatura")
- `profesor` → User
- `matriculas` → AsignaturaEstudiante (back_populates="asignatura")

### Postulacion
- `convocatoria` → Convocatoria (back_populates="postulaciones")
- `estudiante` → User (back_populates="postulaciones")
- `archivos` → ArchivoAdjunto (back_populates="postulacion", cascade="all, delete-orphan")

### ArchivoAdjunto
- `postulacion` → Postulacion (back_populates="archivos")
- `usuario` → User (back_populates="archivos")

### AsignaturaEstudiante
- `asignatura` → Asignatura (back_populates="matriculas")
- `estudiante` → User

## Diagrama Entidad-Relación (Resumen)

```
User (1) ----< (N) Postulacion >---- (1) Convocatoria >---- (1) Asignatura
User (1) ----< (N) ArchivoAdjunto >---- (0,1) Postulacion
User (1) ----< (N) AsignaturaEstudiante >---- (1) Asignatura
User (1) ----< (N) Convocatoria
User (1) ----< (N) Asignatura (profesor)
```

## Cumplimiento de Requisitos

✅ **Foreign Keys**: Todas las relaciones están definidas con FK explícitas
✅ **Unique Constraints**: Campos únicos y restricciones de unicidad compuesta
✅ **Nullable**: Campos obligatorios marcados con nullable=False
✅ **Check Constraints**: Validaciones de rango y dominio implementadas
✅ **Indexes**: Índices en campos frecuentemente consultados
✅ **Cascade**: Borrado en cascada configurado en relaciones dependientes
