from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from loguru import logger
import numpy as np

# Configuración del logger
logger.add("api.log", rotation="500 MB")

app = FastAPI(
    title="API de Clasificación de Vinos",
    description="API para predecir la clase de vino usando el dataset de sklearn",
    version="1.0.0"
)

# Cargar y preparar los datos
X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

@app.post("/predict")
async def predict_wine(features: WineFeatures):
    try:
        logger.info(f"Recibiendo predicción para características: {features}")
        
        # Convertir características a array
        X = np.array([
            features.alcohol, features.malic_acid, features.ash, features.alcalinity_of_ash,
            features.magnesium, features.total_phenols, features.flavanoids, features.nonflavanoid_phenols,
            features.proanthocyanins, features.color_intensity, features.hue, 
            features.od280_od315_of_diluted_wines, features.proline
        ]).reshape(1, -1)
        
        # Realizar predicción
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]
        
        # Mapear clases a tipos de vino
        wine_types = {0: "Clase 0", 1: "Clase 1", 2: "Clase 2"}
        
        result = {
            "prediction": int(prediction),
            "probabilities": {f"clase_{i}": float(prob) for i, prob in enumerate(probabilities)},
            "message": f"Vino clasificado como: {wine_types[prediction]}"
        }
        
        logger.info(f"Predicción exitosa: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Error durante la predicción: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"}