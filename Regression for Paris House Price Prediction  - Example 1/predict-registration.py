import pureml

api_key = " " # Enter Your API ID
organization_id = "" # Enter YOur Organization ID


pureml.login(org_id=organization_id, api_token=api_key)

pureml.predict.add(label='Regressionexample2_model:development', paths={'predict': './predict.py'})
