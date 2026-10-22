# Sistema Integrado de Prácticas Académicas y Monitorías (SIPAM)

Sistema web para la gestión integral de prácticas académicas y monitorías de la Universidad Surcolombiana.

## 📋 Descripción

SIPAM es una plataforma que permite gestionar el ciclo completo de prácticas y monitorías, desde la convocatoria hasta la evaluación final, con roles diferenciados para estudiantes, profesores, jefes de programa, decanos y administradores.

## 🏗️ Arquitectura

### Backend (Python/FastAPI)
- **Framework**: FastAPI 0.115+ con Uvicorn
- **Base de datos**: SQLAlchemy 2.0 (SQLite en desarrollo, PostgreSQL en producción)
- **Autenticación**: JWT (PyJWT) con bcrypt para hashing de contraseñas
- **Organización modular**:
  ```
  backend/
  ├── app/
  │   ├── api/v1/      # Endpoints REST
  │   ├── core/        # Configuración y seguridad (JWT)
  │   ├── db/          # SQLAlchemy engine y sesiones
  │   ├── models/      # Modelos ORM y constraints
  │   ├── schemas/     # Esquemas Pydantic
  │   ├── services/    # Lógica de negocio
  │   └── utils/       # Utilidades
  ├── uploads/         # Archivos subidos (fotos, documentos)
  └── requirements.txt
  ```

### Frontend (React/TypeScript)
- **Framework**: React 19 + TypeScript
- **Bundler**: Vite 8.0
- **Estilos**: TailwindCSS 4.2
- **Estado**: Redux + Redux Thunk
- **Rutas**: React Router DOM
- **Organización**:
  ```
  frontend/
  ├── src/
  │   ├── components/  # Componentes reutilizables
  │   ├── context/     # Contextos globales (Auth, System)
  │   ├── hooks/       # Custom hooks
  │   ├── pages/       # Páginas de la aplicación
  │   ├── services/    # Cliente Axios
  │   ├── types/       # Interfaces TypeScript
  │   └── utils/       # Utilidades
  └── package.json
  ```

## 🚀 Stack Tecnológico

| Categoría | Tecnología |
|-----------|------------|
| **Backend** | Python 3.13, FastAPI, SQLAlchemy 2.0 |
| **Frontend** | React 19, TypeScript, Vite, TailwindCSS |
| **Base de datos** | SQLite (dev), PostgreSQL (prod) |
| **Autenticación** | JWT (PyJWT), bcrypt |
| **API Docs** | FastAPI automatic OpenAPI/Swagger |
| **Librerías adicionales** | Leaflet (mapas), Recharts (gráficos), jsPDF (reportes) |

## 👥 Roles de Usuario

El sistema cuenta con los siguientes roles:

- **Admin**: Gestión completa del sistema
- **Estudiante**: Postulación a convocatorias, registro de horas de monitoría
- **Profesor**: Evaluación de monitores, seguimiento de prácticas
- **Jefe de Programa**: Gestión de presupuestos y aprobaciones
- **Decano**: Reportes y autorizaciones

Las credenciales de prueba se configuran mediante variables de entorno locales. Ver `.env.example` para configuración.

## 🔐 Seguridad

- Autenticación JWT con tokens de acceso
- Hashing de contraseñas con bcrypt
- CORS configurado para orígenes permitidos
- Headers de seguridad (X-Frame-Options, HSTS, etc.)
- Variables de entorno sensibles protegidas con `.gitignore`

## 📦 Instalación

### Prerrequisitos
- Python 3.13+
- Node.js 20+
- PostgreSQL (para producción)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env con tus credenciales
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🧪 Pruebas

Ejecutar pruebas unitarias:
```bash
cd backend
pytest
```

## 📄 Módulos

- **Convocatorias**: Gestión de convocatorias de prácticas y monitorías
- **Postulaciones**: Estudiantes postulan a convocatorias
- **Prácticas**: Seguimiento de prácticas académicas
- **Evaluaciones**: Evaluación de monitores por profesores
- **Presupuesto**: Gestión de viáticos y presupuesto
- **Transporte**: Cálculo de costos de transporte con integración SICOM
- **Monitorías**: Registro de horas de monitoría
- **Notificaciones**: Sistema de alertas automáticas
- **Reportes**: Generación de reportes y estadísticas
- **Calendario**: Gestión de eventos y fechas

## 🔧 Automatizaciones

El backend incluye tareas programadas con APScheduler:
- Actualización diaria de precios de combustible desde SICOM
- Envío de recordatorios de convocatorias próximas a cerrar

## 📝 Licencia

Universidad Surcolombiana - 2026
