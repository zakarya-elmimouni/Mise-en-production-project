# src/train.py

import argparse
import mlflow
import mlflow.sklearn
from src.data.load_data import S3DataLoader
from src.models.train_model import ModelTrainer
import sys
import os

# Ajoute le dossier racine du projet dans le PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

BUCKET = "arazig"
TRAIN_FILE = "projet-mise-en-prod/data/train.csv"
TARGET_COL = "relative_humidity"


def main(remote_server_uri: str, experiment_name: str):
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run():
        # Log des paramètres
        mlflow.log_param("bucket", BUCKET)
        mlflow.log_param("train_file", TRAIN_FILE)

        # Chargement
        loader = S3DataLoader(BUCKET)
        train_df = loader.load_csv(TRAIN_FILE)

        # Entraînement avec tuning
        tuner = ModelTrainer(TARGET_COL)
        model = tuner.fine_tune(train_df)

        # Log du modèle et hyperparams
        mlflow.log_params(tuner.best_params_)
        mlflow.sklearn.log_model(model, "model")

        print("✅ Modèle loggé avec succès !")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote_server_uri", type=str, required=True)
    parser.add_argument("--experiment_name", type=str, required=True)
    args = parser.parse_args()

    main(args.remote_server_uri, args.experiment_name)
