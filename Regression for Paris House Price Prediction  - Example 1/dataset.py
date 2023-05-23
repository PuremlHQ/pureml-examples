# This Repository Contains the Dataset Creation for the Regression task using pureml

import pureml
import pandas as pd
from sklearn.model_selection import train_test_split
from pureml.decorators import dataset, load_data


api_key = " " # Enter Your API ID
organization_id = "" # Enter YOur Organization ID


pureml.login(org_id=organization_id, api_token=api_key)

@load_data()
def load_data():
    train_df = pd.read_csv('./data/train.csv')
    return train_df


@dataset(label='Regression_example_1_data:development', upload=True)
def dataset():
    df = load_data()
    features = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'cityPartRange', 'cityCode', 'floors',
                'numPrevOwners', 'made', 'isNewBuilt',
                'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom', 'hasGuestRoom']
    y = df['price']
    x_train, x_test, y_train, y_test = train_test_split(df[features], df['price'], test_size=0.25)
    return {"x_train": x_train, "x_test": x_test, "y_train": y_train, "y_test": y_test}


df = dataset()
# df = pureml.dataset.fetch('Regression_example_1_data:development') #To Fetch the dataset.
x_train = df['x_train']
x_test = df['x_test']
y_train = df['y_train']
y_test = df['y_test']
