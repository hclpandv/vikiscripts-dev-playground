#!/usr/bin/env python
import os
from azure.identity import ManagedIdentityCredential, EnvironmentCredential, ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from azure.cli.core import get_default_cli

auth_method = "sp" # or msi or az_cli

if auth_method == "msi":
    credentials = ManagedIdentityCredential()
    # credential = DefaultAzureCredential()
elif auth_method == "sp":
    #subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', None),
    client_id = os.environ.get('CLIENT_ID', None),
    client_secret = os.environ.get('CLIENT_SECRET', None),
    tenant_id = os.environ.get('TENANT_ID', None)
    credentials = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)
elif auth_method == "az_cli":
    cli_credentials = get_default_cli()
    #cli_credentials = get_default_cli().invoke(['login', '--use-device-code'])
    credentials = cli_credentials.get_authentication_token()
else:
    print("Please define the auth_method variable or pass it as a  parameter")


vault_url = "https://vikivault01.vault.azure.net"
secret_client = SecretClient(vault_url=vault_url, credential=credentials)
secret = secret_client.get_secret("vikisecret")
print(secret.value)