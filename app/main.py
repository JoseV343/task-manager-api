from fastapi import FastAPI
from app.db.session import engine, Base
from app.routers import auth, tasks

# Crea las tablas en la base de datos al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="API REST para gestión de tareas con autenticación JWT",
    version="1.0.0",
)

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/", tags=["Health"])
def root():
    return {"message": "Task Manager API funcionando ✅"}