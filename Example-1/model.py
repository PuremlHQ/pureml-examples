# Model Creation & Registraion for the Registered Dataset in PureMl

import pureml
import numpy as np
from sklearn.metrics import mean_squared_error
from pureml.decorators import model
import xgboost as xgb
from dataset import x_test, x_train, y_train, y_test


api_key = " " # Enter Your API ID
organization_id = "" # Enter YOur Organization ID


pureml.login(org_id=organization_id, api_token=api_key)


@model(label='Regression_example_1_model:development')
def train_model():
    MODEL_PARAMS = {
        'booster': 'gbtree',
        'learning_rate': 0.11,
        'n_estimators': 77,
        'objective': 'reg:squarederror',
        'gamma': 1,
        'max_depth': 4,
        'reg_lambda': 1,
        'reg_alpha': 1,
        'subsample': 0.85,
        'colsample_bytree': 1,
        'min_child_weight': 2,
        'seed': 42
    }
    xgbr = xgb.XGBRegressor(**MODEL_PARAMS)
    xgbr.fit(x_train, y_train)
    ypred2 = xgbr.predict(x_test)
    rmse = np.sqrt(mean_squared_error(y_test, ypred2))
    pureml.log(metrics={'RMSE': rmse})
    print(f"RMSE: {rmse}")
    return xgbr


trained_model = train_model()
# trained_model = pureml.model.fetch('Regression_example_1_model:development') # To Fetch the Registered Model.
# print(type(trained_model))
