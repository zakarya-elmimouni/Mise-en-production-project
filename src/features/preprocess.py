import pandas as pd
from sklearn.preprocessing import FunctionTransformer


class DateFeatureExtractor:
    def __call__(self, df):
        df = df.copy()
        df["valid_time"] = pd.to_datetime(df["valid_time"])
        df["year"] = df["valid_time"].dt.year
        df["month"] = df["valid_time"].dt.month
        df["day"] = df["valid_time"].dt.day
        return df.drop(columns=["valid_time"])

datetime_transformer = FunctionTransformer(DateFeatureExtractor())
