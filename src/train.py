import argparse
import mlflow
import mlflow.sklearn
from src.data.load_data import S3DataLoader
from src.models.train_model import ModelTrainer
import sys
import os
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main(remote_server_uri, experiment_name, run_name, cv, bucket, train_path, test_path, target_col):
    # Setup MLflow
    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name=run_name):
        # Log des paramètres
        mlflow.log_param("cv", cv)
        mlflow.log_param("bucket", bucket)
        mlflow.log_param("train_path", train_path)
        mlflow.log_param("test_path", test_path)
        mlflow.log_param("target_col", target_col)

        # Chargement des données
        loader = S3DataLoader(bucket)
        train_df = loader.load_csv(train_path)
        test_df = loader.load_csv(test_path)

        # Entraînement
        tuner = ModelTrainer(target_col, cv=cv)
        model = tuner.fine_tune(train_df)

        # Évaluation
        X_test = test_df[tuner.features]
        y_test = test_df[target_col]
        y_pred = model.predict(X_test)

        rmse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        # Logging
        mlflow.log_params(tuner.best_params_)
        mlflow.sklearn.log_model(model, "model")

        print("✅ Modèle entraîné et loggé avec succès.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--remote_server_uri", type=str, required=True)
    parser.add_argument("--experiment_name", type=str, required=True)
    parser.add_argument("--run_name", type=str, default="default-run")
    parser.add_argument("--cv", type=int, default=5)
    parser.add_argument("--bucket", type=str, required=True)
    parser.add_argument("--train_path", type=str, required=True)
    parser.add_argument("--test_path", type=str, required=True)
    parser.add_argument("--target_col", type=str, required=True)

    args = parser.parse_args()

    main(
        args.remote_server_uri,
        args.experiment_name,
        args.run_name,
        args.cv,
        args.bucket,
        args.train_path,
        args.test_path,
        args.target_col
    )
