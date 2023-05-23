import pureml


api_key = " " # Enter Your API ID
organization_id = "" # Enter YOur Organization ID

pureml.login(org_id=organization_id, api_token=api_key)

pureml.eval(task_type='regression',
                   label_model='Regression_example_1_model:development',
                   label_dataset='Regression_example_1_data:development')

