# Documentación de Pruebas Unitarias - SIPAM

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias del backend:

```bash
cd backend
pytest tests/ -v
```

## Estructura de Pruebas

La carpeta `backend/tests/` contiene las siguientes pruebas:

- `test_api.py` - Pruebas de endpoints API básicos
- `test_api_full.py` - Pruebas integrales de la API
- `test_usuarios.py` - Pruebas específicas del módulo de usuarios
- `conftest.py` - Configuración de fixtures para pytest

## Fixtures Disponibles

### `db_session`
Proporciona una sesión de base de datos SQLite temporal para cada prueba.

### `client`
Proporciona un cliente de prueba FastAPI con la base de datos de prueba inyectada.

## Cobertura de Pruebas

Las pruebas cubren:

1. **Autenticación**: Login, registro, validación de tokens
2. **Usuarios**: CRUD de usuarios, roles, permisos
3. **Convocatorias**: Creación, actualización, estados
4. **Postulaciones**: Creación, estados, evaluaciones
5. **Validaciones**: Constraints de base de datos, reglas de negocio

## Resultados de Ejecución

Ejecutar las pruebas con reporte de cobertura:

```bash
pytest tests/ --cov=app --cov-report=html
```

Los resultados se generarán en `htmlcov/index.html`.
