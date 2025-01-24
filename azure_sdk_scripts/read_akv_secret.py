#!/usr/bin/env python
"""
Description : Module to read AKV Secret
Version     : 1.0
Maintainer  : Vikas Pandey, <vikiscripts@gmail.com>
Date        : 17-MAR-2023
"""
from os import environ as env
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

TENANT_ID = env.get("TENANT_ID", "")
CLIENT_ID = env.get("CLIENT_ID", "")
CLIENT_SECRET = env.get("CLIENT_SECRET", "")

KEYVAULT_URI = "https://vikikeyvault01.vault.azure.net/"

_credential = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)
DEMO_DB_PASSWORD = _sc.get_secret("vikisecret").value

print(DEMO_DB_PASSWORD)