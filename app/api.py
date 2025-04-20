import os
import sys
from fastapi import FastAPI
import mlflow
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

mlflow.set_tracking_uri("https://user-akhairaldin-mlflow.user.lab.sspcloud.fr")

# Preload model -------------------
MODEL_NAME = "production"
MODEL_STAGE = "latest"

model_uri = f"models:/{MODEL_NAME}/{MODEL_STAGE}"
model = mlflow.sklearn.load_model(model_uri)

# Define app -------------------------
app = FastAPI(
    title="API de prédiction de l'humidité relative",
    description="Prédiction de l'humidité relative en fonction de données météorologiques",
    version="0.1"
)

@app.get("/", tags=["Accueil"])
def read_root():
    return {
        "message": "API de prédiction de l'humidité relative",
        "model": MODEL_NAME,
        "version": MODEL_STAGE
    }

@app.get("/predict", tags=["Prédiction"])
async def predict(
    latitude: float,
    longitude: float,
    temperature: float,
    divergence: float,
    u_component_wind: float,
    v_component_wind: float,
    valid_time: str
):
    """
    Effectue une prédiction à partir des paramètres météorologiques
    """
    input_data = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "temperature": temperature,
        "divergence": divergence,
        "u_component_wind": u_component_wind,
        "v_component_wind": v_component_wind,
        "valid_time": valid_time
    }])
    
    prediction = model.predict(input_data)[0]
    return {"prediction": float(prediction)}