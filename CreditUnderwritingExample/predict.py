from pureml import BasePredictor, Input, Output
import pureml
from typing import Any


class Predictor(BasePredictor):
    label:Any = "Credit Model Underwriting:v1"
    input:Any = Input(type="numpy ndarray")
    output:Any = Output(type="numpy ndarray")

    def load_models(self):
        self.model = pureml.model.fetch(self.label)


    def predict(self, data):
        predictions = self.model.predict(data)

        return predictions
