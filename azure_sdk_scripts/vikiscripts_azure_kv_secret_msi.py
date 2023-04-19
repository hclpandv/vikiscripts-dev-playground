#!/usr/bin/env python
"""read password secret from Azure Key Vault"""
import azure.identity
import azure.keyvault.secrets

VAULT_URL = "https://vikikeyvault01.vault.azure.net"
SECRET_NAME = "vikisecret"

DB_PASSWORD = azure.keyvault.secrets.SecretClient(
    vault_url=VAULT_URL,
    credential=azure.identity.ManagedIdentityCredential()
).get_secret(SECRET_NAME).value

print(DB_PASSWORD)
