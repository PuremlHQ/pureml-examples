#!/bin/bash

# Create and activate virtual environment
python3 -m venv puremltest
source puremltest/bin/activate

# # Install packages from requirements.txt
pip install -r requirements.txt

pureml auth login 


# Integration details
integration_number=2               
secret_name=""
access_key_id=""
access_key_secret=""
account_id=""
bucket_name=""
public_url=""

# Add secrets using PureML
pureml secrets add <<EOF
$integration_number
$secret_name
$access_key_id
$access_key_secret
$account_id
$bucket_name
$public_url
EOF

# PureML initialization
storage_repository=3
added_secrets="y"
name_of_integration_secret="$secret_name"
self_hosted="N"

# PureML Init
pureml init <<EOF
$storage_repository
$added_secrets
$name_of_integration_secret
$self_hosted
EOF

