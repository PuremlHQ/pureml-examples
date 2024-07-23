#!/bin/bash

#Create and activate virtual environment
python3 -m venv puremltest
source puremltest/bin/activate

#Install packages from requirements.txt
pip install -r requirements.txt

pureml auth login 



# PureML initialization
storage_repository=1
local_repository = "pureml_data"
added_secrets="y"
name_of_integration_secret="$secret_name"
self_hosted="N"

# PureML Init
pureml init <<EOF
$storage_repository
$local_repository
$self_hosted
EOF

