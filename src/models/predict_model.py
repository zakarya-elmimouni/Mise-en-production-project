class ModelPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, test_df):
        return self.model.predict(test_df)
