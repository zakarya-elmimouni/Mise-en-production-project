import argparse
from src.data.load_data import S3DataLoader
from src.models.train_model import ModelTrainer
from src.models.predict_model import ModelPredictor
from src.evaluation.evaluate import ModelEvaluator
from sklearn.model_selection import GridSearchCV


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
target = args.target_col

# Chargement des données
print("Chargement des données...")
loader = S3DataLoader(args.bucket, args.endpoint_url)
train_df = loader.load_csv(args.train_file)
test_df = loader.load_csv(args.test_file)

# Définition des variables target et explicatives
X_train, y_train = train_df.drop(columns=target), train_df[target]
X_test, y_test = test_df.drop(columns=target), test_df[target]

# Cross-validation
print('Cross-validation en cours...')
pipe = ModelTrainer(target).build_pipeline()
param_grid = {
    "randomforestregressor__n_estimators": [10, 20, 25],
    "randomforestregressor__max_depth": [5, 8, 10]
}

pipe_cross_validation = GridSearchCV(
    pipe,
    param_grid=param_grid,
    scoring='neg_root_mean_squared_error',
    cv=3,
    n_jobs=-1,
    verbose=1,
)

pipe_cross_validation.fit(X_train, y_train)

pipe = pipe_cross_validation.best_estimator_


'''# Entraînement du modèle
print("Entraînement du modèle...")
trainer = ModelTrainer(args.target_col)
model = trainer.train(train_df)'''

# Evaluation
print('Evaluation du meilleur modèle')
predictions = pipe(X_test)
evaluator = ModelEvaluator(test_df[target], predictions)
metrics = evaluator.evaluate()
print(metrics)

'''# Prédictions
print("Prédictions...")
predictor = ModelPredictor(model)
predictions = predictor.predict(test_df)
print(predictions[:5])

# Évaluation
print("Évaluation du modèle...")
evaluator = ModelEvaluator(test_df[args.target_col], predictions)
metrics = evaluator.evaluate()
print(metrics)'''
