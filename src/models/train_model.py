import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from src.features.preprocess import datetime_transformer


class ModelTrainer:
    def __init__(self, target_col: str, cv: int = 3):
        self.target_col = target_col
        self.features = [
            'latitude', 'longitude', 'temperature', 'divergence',
            'u_component_wind', 'v_component_wind', 'valid_time'
        ]
        self.pipeline = self.build_pipeline()
        self.cv = cv

    def build_pipeline(self):
        preprocessor = make_column_transformer(
            (datetime_transformer, ['valid_time']),
            remainder='passthrough'
        )

        return make_pipeline(
            preprocessor,
            SimpleImputer(),
            RandomForestRegressor(max_depth=5, n_estimators=10)
        )

    def train(self, df: pd.DataFrame):
        X = df[self.features]
        y = df[self.target_col]
        pipeline = self.build_pipeline()
        pipeline.fit(X, y)
        return pipeline

    def fine_tune(self, df: pd.DataFrame, param_grid: dict = None, cv: int = 2):
        if param_grid is None:
            param_grid = {
                "randomforestregressor__n_estimators": [10,15],
                "randomforestregressor__max_depth": [10, 15],
                "randomforestregressor__min_samples_split": [2, 4],
            }

        X = df[self.features]
        y = df[self.target_col]

        self.pipeline = self.build_pipeline()

        grid_search = GridSearchCV(
            self.pipeline,
            param_grid,
            cv=cv,
            scoring='neg_root_mean_squared_error',
            n_jobs=-1,
            verbose=2
        )

        grid_search.fit(X, y)
        self.best_model_ = grid_search.best_estimator_
        self.best_params_ = grid_search.best_params_
        self.cv_results_ = grid_search.cv_results_

        return self.best_model_
