"""Punto de entrada de la API. Ejecutar con: uvicorn app.main:app --reload"""

from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(
    title="House Pricing API",
    description="Predicciones en línea del precio de viviendas.",
    version="0.1.0",
)

app.include_router(health.router)
