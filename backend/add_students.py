"""
SIPAM-USCO — Script aditivo: agrega estudiantes a materias con pocos inscritos.
Ejecutar con el servidor EN EJECUCIÓN o detenido:
    venv/Scripts/python add_students.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(__file__))

from app.db.database import SessionLocal, init_db
from app.models.user import User, RolEnum
from app.models.convocatoria import Asignatura, AsignaturaEstudiante
from app.core.security import get_password_hash

random.seed(99)
PERIODO = "2026-1"
PW      = get_password_hash("sipam2025")
MIN_EST = 10   # mínimo deseado de estudiantes por materia

# Asignaciones: materia_codigo → año de ingreso de los nuevos estudiantes
MATERIA_ANIO = {
    "ISW-101": 2023, "ISW-201": 2023, "ISW-202": 2022,
    "MAT-101": 2023, "MAT-201": 2022, "ISW-301": 2021,
    "ISW-302": 2020, "ISW-401": 2020, "ISW-402": 2019,
    "ISW-501": 2019, "ISW-502": 2019, "ISW-601": 2018,
    "ISW-602": 2018, "ISW-701": 2018, "MAT-301": 2020,
    "MAT-401": 2021, "ISW-303": 2017, "ISW-403": 2017,
    "ISW-503": 2016, "ISW-603": 2016,
}

_NOMS = ["Andrés","Beatriz","Carlos","Diana","Ernesto","Fabiana","Gonzalo",
         "Helena","Ignacio","Juliana","Kevin","Lorena","Mario","Nathalia",
         "Oscar","Patricia","Ramón","Sandra","Tomás","Úrsula"]
_APES = ["Agudelo","Botero","Cárdenas","Daza","Estupiñán","Fuentes",
         "Galindo","Hernández","Izquierdo","Jiménez","Kukuli","Lara",
         "Montoya","Noriega","Orozco","Pulido","Quiroga","Rosales",
         "Sandoval","Torres"]

def run():
    init_db()
    db = SessionLocal()
    try:
        asignaturas = db.query(Asignatura).filter(Asignatura.is_active == True).all()
        total_nuevos = 0

        for asig in asignaturas:
            actuales = db.query(AsignaturaEstudiante).filter(
                AsignaturaEstudiante.asignatura_id == asig.id,
                AsignaturaEstudiante.periodo_academico == PERIODO,
            ).count()

            faltan = max(0, MIN_EST - actuales)
            if faltan == 0:
                print(f"  ✓  {asig.codigo:10} — {asig.nombre[:35]:35} {actuales:3} est. (OK)")
                continue

            print(f"  +  {asig.codigo:10} — {asig.nombre[:35]:35} {actuales:3} → +{faltan}")
            anio_base = MATERIA_ANIO.get(asig.codigo, 2022)

            for j in range(faltan):
                nom = _NOMS[(total_nuevos + j) % len(_NOMS)]
                ape = _APES[(total_nuevos + j) % len(_APES)]
                num = 500 + total_nuevos + j
                codigo = f"{anio_base}1150A{num:03d}"

                # Evitar duplicados de código
                if db.query(User).filter(User.codigo == codigo).first():
                    codigo = f"{anio_base}1150B{num:03d}"
                if db.query(User).filter(User.codigo == codigo).first():
                    continue

                prom = round(random.uniform(2.8, 5.0), 2)
                pct  = round(random.uniform(20.0, 90.0), 1)
                cedula = f"119{num + 800000:07d}"

                est = User(
                    codigo=codigo, nombres=nom, apellidos=ape,
                    email=f"{nom.lower()}.{ape.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')}{num}@usco.edu.co",
                    cedula=cedula, hashed_password=PW,
                    rol=RolEnum.estudiante, promedio=prom,
                    porcentaje_creditos=pct,
                    programa="Ingeniería de Software", sede="Neiva",
                )
                db.add(est)
                db.flush()

                db.add(AsignaturaEstudiante(
                    asignatura_id=asig.id,
                    estudiante_id=est.id,
                    periodo_academico=PERIODO,
                ))
                total_nuevos += 1

        db.commit()
        print(f"\n  ✓  {total_nuevos} nuevos estudiantes/matrículas creados en {PERIODO}.")

        # Resumen final
        print("\n  Cobertura final por materia:")
        for asig in db.query(Asignatura).filter(Asignatura.is_active == True).order_by(Asignatura.semestre).all():
            n = db.query(AsignaturaEstudiante).filter(
                AsignaturaEstudiante.asignatura_id == asig.id,
                AsignaturaEstudiante.periodo_academico == PERIODO,
            ).count()
            bar = "█" * (n // 3)
            print(f"    {asig.codigo:10} {asig.nombre[:30]:30} {n:3} {bar}")

    except Exception as e:
        db.rollback()
        print(f"\n  ✗ ERROR: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    run()
