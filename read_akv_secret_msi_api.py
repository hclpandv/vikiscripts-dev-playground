#!/usr/bin/env python
"""read password secret from Azure Key Vault"""
import requests

url = 'http://169.254.169.254/metadata/identity/oauth2/token'
params = {
    'api-version': '2018-02-01',
    'resource': 'https://vault.azure.net'
}
headers = {'Metadata': 'true'}
response = requests.get(url, params=params, headers=headers)
access_token = response.json()['access_token']


SECRET_NAME = "ansibleid"
VAULT_URL = "https://some-vault.vault.azure.net/secrets/{}?api-version=7.1".format(SECRET_NAME)

headers = {"Authorization": "Bearer {}".format(access_token)}
response = requests.get(VAULT_URL, headers=headers)

DB_PASSWORD = response.json()['value']

print(DB_PASSWORD)
