#!/usr/bin/env python
"""
Description : Module to read AKV Secret
Version     : 1.0
Maintainer  : Vikas Pandey, <vikiscripts@gmail.com>
Date        : 11-Jun-2023
"""
from os import environ as env
import requests

TENANT_ID = env.get("TENANT_ID", "")
CLIENT_ID = env.get("CLIENT_ID_CONTRIB", "")
CLIENT_SECRET = env.get("CLIENT_SECRET_CONTRIB", "")

# Configure the storage account settings
account_name = 'tfstate1395347833'
container_name = 'vikitest'
blob_name = 'resources.csv'
local_file_path = 'resources.csv'

# Authenticate with the service principal
token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"
token_data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'resource': f"https://{account_name}.blob.core.windows.net"
}
token_response = requests.post(token_url, data=token_data)
token_response.raise_for_status()
access_token = token_response.json()['access_token']

#print(access_token)

# Upload the file to the blob
upload_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}"
headers = {
    'Authorization': 'Bearer ' + access_token,
    'x-ms-blob-type': 'BlockBlob',
    'x-ms-version': '2020-04-08'
}
with open(local_file_path, 'rb') as file:
    response = requests.put(upload_url, data=file, headers=headers)
response.raise_for_status()

print("File uploaded successfully.")
