import sqlite3
conn = sqlite3.connect("sipam_usco.db")
c = conn.cursor()
TABLES = ["users","asignaturas","asignatura_estudiantes","convocatorias","postulaciones","presupuestos","practicas","horas_monitor"]
for t in TABLES:
    try:
        c.execute(f"SELECT COUNT(*) FROM {t}")
        print(f"  {t:<30} {c.fetchone()[0]:>5} filas")
    except Exception as e:
        print(f"  {t:<30} ERROR: {e}")
c.execute("SELECT rol, COUNT(*) FROM users GROUP BY rol")
print("Users por rol:", dict(c.fetchall()))
conn.close()
