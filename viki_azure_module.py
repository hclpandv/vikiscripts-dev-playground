#!/usr/bin/env python
"""
Description : Module to interact with AzureRM via rest api
Version     : 1.0
Date        : 24-FEB-2023
"""
import json
import os
#import re
import requests

class VikiAzureRM:
    """
    Rest API interaction with AzureRM
    """
    def __init__(self, subscription_id,client_id,client_secret,tenant_id):
        self.subscription_id = subscription_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
    
    def get_azure_token(self):
        """
        Function to Authenticate Azure and get token
        """
        # Request a token for authentication
        token_endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(self.tenant_id)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "resource": "https://management.azure.com/"
        }
        response = requests.post(token_endpoint, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception("Failed to get authentication token")
        token = response.json()["access_token"]
        return token
    
    def get_azure_rgs(self):
        """
        Function to retrive all resourceGroups in a subscription
        """
        token = self.get_azure_token()
        headers = {
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json"
        }

        rgs = []
        rg_endpoint = "https://management.azure.com/subscriptions/{}/resourcegroups?api-version=2021-04-01".format(self.subscription_id)
        response = requests.get(rg_endpoint, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to get list of Resource Groups")
        result = response.json()
        if 'value' in result:
            rgs.extend(result['value'])
        return json.dumps(rgs, indent=4)

    def get_azure_vms(self,resource_group_name=None):
        """
        Function to retrive all VMs in a subscription or resource group
        """
        if(resource_group_name):
            output = "Getting all VMs from resource group: {}".format(resource_group_name)
        else:
            output = "Getting all VMs from subscription: {}".format(self.subscription_id)
        return output
    
    @property
    def name(self):
        """
        Function to respond title.
        """
        return self.subscription_id
    # The title() method is a built-in string method in Python that returns a copy of the string
    # with the first letter of each word capitalized and the rest of the letters in lowercase.


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
    print(my_instance.get_azure_rgs())
