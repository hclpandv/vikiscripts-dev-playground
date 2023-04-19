#!/usr/bin/env python
"""read password secret from Azure Key Vault"""
import os
import azure.identity
import azure.keyvault.secrets

VAULT_URL = "https://vikikeyvault01.vault.azure.net"
SECRET_NAME = "vikisecret"

DB_PASSWORD = azure.keyvault.secrets.SecretClient(
    vault_url=VAULT_URL,
    credential=azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
    )
).get_secret(SECRET_NAME).value

print(DB_PASSWORD)
