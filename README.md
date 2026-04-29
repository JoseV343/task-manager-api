# 📋 Task Manager API

API REST para gestión de tareas personales con autenticación JWT, construida con FastAPI y MySQL.

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Framework | FastAPI 0.111 |
| Base de datos | MySQL 8+ |
| ORM | SQLAlchemy 2.0 |
| Autenticación | JWT (python-jose) |
| Seguridad | Bcrypt (passlib) |
| Servidor | Uvicorn |
| Validación | Pydantic v2 |

## ⚙️ Instalación

1. Clona el repo: `git clone https://github.com/JoseV343/task-manager-api.git`
2. Crea el entorno virtual: `py -m venv venv`
3. Actívalo: `source venv/Scripts/activate`
4. Instala dependencias: `pip install -r requirements.txt`
5. Copia el env: `cp .env.example .env` y edítalo con tus credenciales
6. Crea la BD en MySQL: `CREATE DATABASE task_manager_db`
7. Levanta el servidor: `uvicorn app.main:app --reload`

## 📖 Documentación

Swagger UI disponible en `http://localhost:8000/docs`

## 🔐 Endpoints Auth

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/register` | Registra un usuario |
| POST | `/auth/login` | Login y obtiene JWT |

## ✅ Endpoints Tareas (requieren JWT)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/tasks/` | Crea una tarea |
| GET | `/tasks/` | Lista las tareas |
| GET | `/tasks/{id}` | Obtiene una tarea |
| PUT | `/tasks/{id}` | Actualiza una tarea |
| DELETE | `/tasks/{id}` | Elimina una tarea |

## 👨‍💻 Autor

**Davier** — Desarrollador Full Stack Junior  
Stack: Python · FastAPI · MySQL · APIs REST