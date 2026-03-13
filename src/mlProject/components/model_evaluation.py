from sklearn.metrics import r2_score, mean_absolute_error
from src.mlProject.logger import logging


class ModelEvaluation:

    def evaluate_model(self, model, X_test, y_test):

        preds = model.predict(X_test)

        r2 = r2_score(y_test, preds)
        mae = mean_absolute_error(y_test, preds)

        logging.info(f"R2 Score: {r2}")
        logging.info(f"MAE: {mae}")

        print("R2 Score:", r2)
        print("MAE:", mae)