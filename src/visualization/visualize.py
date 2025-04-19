import matplotlib.pyplot as plt


class Visualizer:
    @staticmethod
    def plot_feature_importance(model, feature_names):
        importances = model.named_steps['randomforestregressor'].feature_importances_
        plt.figure(figsize=(10, 6))
        plt.barh(feature_names, importances)
        plt.xlabel("Importance")
        plt.title("Feature Importances")
        plt.tight_layout()
        plt.show()
