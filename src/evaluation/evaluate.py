from sklearn.metrics import mean_squared_error, r2_score


class ModelEvaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def evaluate(self):
        rmse = mean_squared_error(self.y_true, self.y_pred, squared=False)
        r2 = r2_score(self.y_true, self.y_pred)
        return {"rmse": rmse, "r2": r2}
