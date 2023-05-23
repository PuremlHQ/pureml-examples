import typing

import pureml
from pureml import BasePredictor, Input, Output

from dataset import x_test, y_test

api_key = " " # Enter Your API ID
organization_id = "" # Enter YOur Organization ID


pureml.login(org_id=organization_id, api_token=api_key)


class Predictor(BasePredictor):
    label = 'Regression_example_1_model:development'
    input = Input(type="pandas dataframe")
    output = Output(type="pandas dataframe")

    def load_models(self):
        self.model = pureml.model.fetch('Regression_example_1_model:development')

    def predict(self, **kwargs: typing.Any):
        prediction = self.model.predict(x_test)
        return prediction
