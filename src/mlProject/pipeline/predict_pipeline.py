import pandas as pd
from src.mlProject.utils import load_object


class PredictPipeline:

    def predict(self, data):

        model = load_object("artifacts/model.pkl")

        predictions = model.predict(data)

        return predictions