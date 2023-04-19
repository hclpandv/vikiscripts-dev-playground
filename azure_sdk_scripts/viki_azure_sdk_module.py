#!/usr/bin/env python
"""
Description : Module to interact with AzureRM via azure SDK
Version     : 1.0
Date        : 18-mar-2023
"""
import os
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


class VikiAzureRM:
    """
    Interaction with AzureRM
    """
    def __init__(self, subscription_id,client_id,client_secret,tenant_id):
        self.subscription_id = subscription_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id

    def get_azure_kv_secret(self,vault_url,secret_name):
        """
        Function to Authenticate Azure and get token
        """
        _credential = ClientSecretCredential(
            tenant_id=self.tenant_id,
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        _sc = SecretClient(vault_url=vault_url, credential=_credential)
        return _sc.get_secret(secret_name).value


if __name__ == '__main__':
    # Example usage
    my_instance = VikiAzureRM(
        client_id = os.environ.get('CLIENT_ID', None),
        client_secret = os.environ.get('CLIENT_SECRET', None),
        tenant_id = os.environ.get('TENANT_ID', None),
        subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
    )

    #Testing    
    #print(my_instance.get_azure_rgs())
    print(my_instance.get_azure_kv_secret("https://vikikeyvault01.vault.azure.net/","vikisecret"))

    password = my_instance.get_azure_kv_secret(
        vault_url = "https://vikikeyvault01.vault.azure.net/",
        secret_name = "vikisecret"
    )
    print(password)
