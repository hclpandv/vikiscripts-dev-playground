#!/usr/bin/env python
"""
Description : Module to read AKV Secret
Version     : 1.0
Maintainer  : Vikas Pandey, <vikiscripts@gmail.com>
Date        : 17-MAR-2023
"""
import os
import azure.identity
import azure.keyvault.secrets

def get_azure_kv_secret(vault_url,secret_name):
    """
    Function to Authenticate Azure and get token
    """
    _credential = azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
    )
    _sc = azure.keyvault.secrets.SecretClient(vault_url=vault_url, credential=_credential)
    return _sc.get_secret(secret_name).value


vault_url = "https://vikikeyvault01.vault.azure.net/"
secret_name = "vikisecret"
print(get_azure_kv_secret(vault_url=vault_url, secret_name=secret_name))