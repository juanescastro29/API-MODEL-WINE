# API de Clasificación de Vinos

Este proyecto implementa una API REST usando FastAPI para desplegar un modelo de clasificación de vinos basado en el dataset de sklearn.

## Requisitos

- Python 3.7+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor:

```bash
python -m uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Endpoints

### POST /predict

Realiza una clasificación de vino basada en las características proporcionadas.

Ejemplo de payload:
```json
{
    "alcohol": 13.0,
    "malic_acid": 1.5,
    "ash": 2.3,
    "alcalinity_of_ash": 15.0,
    "magnesium": 100.0,
    "total_phenols": 2.5,
    "flavanoids": 3.0,
    "nonflavanoid_phenols": 0.3,
    "proanthocyanins": 1.5,
    "color_intensity": 5.0,
    "hue": 1.0,
    "od280_od315_of_diluted_wines": 3.0,
    "proline": 1000.0
}
```

### GET /health

Verifica el estado de la API.

## Documentación

La documentación interactiva de la API está disponible en:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Monitoreo

Los logs de la aplicación se guardan en `api.log` y registran:
- Solicitudes de predicción
- Resultados de predicciones
- Errores y excepciones