import pandas as pd
from src.models.train_model import ModelTrainer

def test_model_trainer_fit_predict():
    # Crée un DataFrame avec les bonnes colonnes
    df = pd.DataFrame({
        "latitude": [45.0, 46.0, 47.0, 48.0],
        "longitude": [1.0, 2.0, 3.0, 4.0],
        "temperature": [12.5, 13.0, 11.8, 14.2],
        "divergence": [0.1, 0.2, 0.15, 0.05],
        "u_component_wind": [2.3, 2.1, 2.5, 2.0],
        "v_component_wind": [1.1, 1.3, 1.0, 1.2],
        "valid_time": [1, 2, 3, 4],
        "humidity": [60, 65, 63, 67]  # Target
    })

    trainer = ModelTrainer(target_col="humidity", cv=2)
    model = trainer.fine_tune(df)

    preds = model.predict(df[trainer.features])
    assert len(preds) == len(df)
