from sklearn.ensemble import RandomForestRegressor
from src.mlProject.utils import save_object
from src.mlProject.logger import logging


class ModelTrainer:

    def initiate_model_trainer(self, X_train, y_train):

        logging.info("Model Training Started")

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        save_object("artifacts/model.pkl", model)

        logging.info("Model Training Completed")

        return model