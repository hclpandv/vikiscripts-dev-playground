#!/usr/bin/env python
"""run command on Azure VM"""
import json
import os
import requests

# Set the subscription ID, resource group name, VM name and run command script
client_id = os.environ.get('CLIENT_ID_CONTRIB', None)
client_secret = os.environ.get('CLIENT_SECRET_CONTRIB', None)
tenant_id = os.environ.get('TENANT_ID', None)
subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
   
resource_group_name = 'Koch_lab'
vm_name = 'Personalserver'
run_command_script = 'get-wmiobject win32_computersystem'

# Set the API version
api_version = '2023-03-01'

# Request a token for authentication
token_endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(tenant_id)
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": "https://management.azure.com/"
}
response = requests.post(token_endpoint, headers=headers, data=data)
if response.status_code != 200:
    raise Exception("Failed to get authentication token")
token = response.json()["access_token"]


# Set the base URL for the Azure RM API
#base_url = 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommand?api-version=2023-03-01
base_url = 'https://management.azure.com/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.Compute/virtualMachines/{2}/runCommand'.format(subscription_id, resource_group_name, vm_name)

# Set the headers for the API request
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

# Set the body of the API request
body = {
    'commandId': 'RunPowerShellScript',
    'script': [
        run_command_script
    ]
}

# Send the API request and get the response
response = requests.post(base_url + '?api-version=' + api_version, headers=headers, data=json.dumps(body))

# Print the message returned by the run command result
print(response.json())
