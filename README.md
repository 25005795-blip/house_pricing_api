# House Pricing API

API para generar predicciones en línea del precio de viviendas con el modelo
`champion` entrenado en el proyecto [House_pricing](https://github.com/25005795-blip/House_pricing).

## Estructura

```
app/
├── main.py            # Crea la app FastAPI y registra los routers
├── api/routes/        # Endpoints (health, predict, ...)
├── core/              # Configuración (variables de entorno)
├── schemas/           # Modelos Pydantic de request/response
└── services/          # Carga del modelo y lógica de predicción
models/                # Artefactos del modelo (no versionados)
tests/                 # Pruebas con pytest
```

## Uso

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Documentación interactiva en http://127.0.0.1:8000/docs
