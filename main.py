from src.data.load_data import S3DataLoader
from src.models.train_model import ModelTrainer
from src.models.predict_model import ModelPredictor
from src.evaluation.evaluate import ModelEvaluator


# Configuration
BUCKET = "mon-bucket"
TRAIN_FILE = "data/train.csv"
TEST_FILE = "data/test.csv"
ENDPOINT_URL = "https://minio.lab.sspcloud.fr"
TARGET_COL = "target"

# Chargement des données
print("Chargement des données...")
loader = S3DataLoader(BUCKET, ENDPOINT_URL)
train_df = loader.load_csv(TRAIN_FILE)
test_df = loader.load_csv(TEST_FILE)

# Entraînement du modèle
print("Entraînement du modèle...")
trainer = ModelTrainer(TARGET_COL)
model = trainer.train(train_df)

# Prédictions
print("Prédictions...")
predictor = ModelPredictor(model)
predictions = predictor.predict(test_df)
print(predictions[:5])

# Évaluation
print("Évaluation du modèle...")
evaluator = ModelEvaluator(test_df[TARGET_COL], predictions)
metrics = evaluator.evaluate()
print(metrics)
