#!/usr/bin/env python
"""Get VM details from Azure"""
import os
import azure.identity
import azure.mgmt.compute

class AzureRM:
    """
    Rest API interaction with AzureRM
    """
    def __init__(self, subscription_id,client_id,client_secret,tenant_id):
        self.subscription_id = subscription_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
    
        self.credential = azure.identity.ClientSecretCredential(
            tenant_id=self.tenant_id,
            client_id=self.client_id,
            client_secret=self.client_secret
        )

        self.compute_client = azure.mgmt.compute.ComputeManagementClient(
            credential=self.credential,
            subscription_id=self.subscription_id
        )
    def get_azure_vm(self,name,resource_group_name):
        """
        Function to retrive all resourceGroups in a subscription
        """
        vm = self.compute_client.virtual_machines.get(
            resource_group_name = resource_group_name,
            vm_name = name
        )
        return vm

    def start_azure_vm(self,name,resource_group_name):
        """
        Function to retrive all resourceGroups in a subscription
        """
        async_vm_start = self.compute_client.virtual_machines.begin_start(
            resource_group_name,
            name
        )

        async_vm_start.wait()
        print("VM {} has been started.".format(name))



if __name__ == '__main__':
    # Example usage
    my_instance = AzureRM(
        client_id = os.environ.get('CLIENT_ID', None),
        client_secret = os.environ.get('CLIENT_SECRET', None),
        tenant_id = os.environ.get('TENANT_ID', None),
        subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
    )
    RESOURCE_GROUP_NAME = 'Koch_lab'
    VM_NAME = 'PersonalServer'  
    
    vm_size = my_instance.get_azure_vm(VM_NAME,RESOURCE_GROUP_NAME).hardware_profile.vm_size
    
    
    print(vm_size)

