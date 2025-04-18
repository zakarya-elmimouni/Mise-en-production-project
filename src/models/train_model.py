import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from src.features.preprocess import datetime_transformer


class ModelTrainer:
    def __init__(self, target_col: str):
        self.target_col = target_col
        self.features = [
            'latitude', 'longitude', 'temperature', 'divergence',
            'u_component_wind', 'v_component_wind', 'relative_humidity', 'valid_time'
        ]

    def build_pipeline(self):
        preprocessor = make_column_transformer(
            (datetime_transformer, ['valid_time']),
            remainder='passthrough'
        )

        return make_pipeline(
            preprocessor,
            SimpleImputer(),
            RandomForestRegressor(random_state=42)
        )

    def train(self, df: pd.DataFrame):
        X = df[self.features]
        y = df[self.target_col]
        pipeline = self.build_pipeline()
        pipeline.fit(X, y)
        return pipeline
