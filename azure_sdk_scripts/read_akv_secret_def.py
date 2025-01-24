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

def get_azure_kv_secret_sp(vault_url,secret_name):
    """
    Function to Authenticate Azure via SP and read secret from keyVault
    """
    _credential = azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
    )
    _sc = azure.keyvault.secrets.SecretClient(vault_url=vault_url, credential=_credential)
    return _sc.get_secret(secret_name).value

def get_azure_kv_secret_msi(vault_url,secret_name):
    """
    Function to Authenticate Azure via MSI and read secret from keyVault
    """
    _credential = azure.identity.ManagedIdentityCredential()
    _sc = azure.keyvault.secrets.SecretClient(vault_url=vault_url, credential=_credential)
    return _sc.get_secret(secret_name).value


VAULT_URI = "https://vikikeyvault01.vault.azure.net/"
SECRET_NAME = "vikisecret"

print(get_azure_kv_secret_sp(vault_url=VAULT_URI, secret_name=SECRET_NAME))
