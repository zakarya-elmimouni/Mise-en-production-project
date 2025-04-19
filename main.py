import argparse
from src.data.load_data import S3DataLoader
from src.models.train_model import ModelTrainer
from src.models.predict_model import ModelPredictor
from src.evaluation.evaluate import ModelEvaluator
from src.models.train_model import ModelTuner


# Fonction pour obtenir les arguments depuis le terminal
def get_args():
    parser = argparse.ArgumentParser(
        description="Exécution du pipeline de prédiction et d'évaluation")
    
    # Ajout des arguments
    parser.add_argument('--bucket', type=str, required=True, help="Nom du bucket S3")
    parser.add_argument('--train_file', type=str, required=True,help="Chemin vers le fichier d'entraînement")
    parser.add_argument('--test_file', type=str, required=True, help="Chemin vers le fichier de test")
    parser.add_argument('--endpoint_url', type=str, required=True, help="URL de l'endpoint S3")
    parser.add_argument('--target_col', type=str, required=True, help="Colonne cible pour l'entraînement")

    return parser.parse_args()

# Récupération des arguments
args = get_args()

# Chargement des données
print("Chargement des données...")
loader = S3DataLoader(args.bucket, args.endpoint_url)
train_df = loader.load_csv(args.train_file)
test_df = loader.load_csv(args.test_file)

# Entraînement du modèle
print("Entraînement du modèle...")
trainer = ModelTrainer(args.target_col)
model = trainer.train(train_df)

# Prédictions
print("Prédictions...")
predictor = ModelPredictor(model)
predictions = predictor.predict(test_df)
print(predictions[:5])

# Évaluation
print("Évaluation du modèle...")
evaluator = ModelEvaluator(test_df[args.target_col], predictions)
metrics = evaluator.evaluate()
print(metrics)


tuner = ModelTuner(target_col=TARGET_COL)
best_model = tuner.fine_tune(train_df)  # Tu peux passer un param_grid personnalisé ici
print("Meilleurs paramètres :", tuner.best_params_)
