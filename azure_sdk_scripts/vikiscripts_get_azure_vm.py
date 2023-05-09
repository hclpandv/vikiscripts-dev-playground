#!/usr/bin/env python
"""Module to Get VM details from Azure"""
import os
import azure.identity
import azure.mgmt.compute

class AzureRM:
    """
    Class to interact with AzureRM and get VM details
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
    def get_azure_vm(self,resource_group_name, name):
        """
        Function to get VM details
        """
        vm = self.compute_client.virtual_machines.get(
            resource_group_name = resource_group_name,
            vm_name = name
        )
        return vm
    
    def get_azure_vm_powerstate(self,resource_group_name, name):
        """
        Function to get VM state
        """
        vm_instance_view = self.compute_client.virtual_machines.instance_view(
            resource_group_name = resource_group_name, 
            vm_name = name
        )
        return vm_instance_view.statuses[1].code

    def start_azure_vm(self,resource_group_name,name):
        """
        Function to start a VM
        """
        async_vm_start = self.compute_client.virtual_machines.begin_start(
            resource_group_name,
            name
        )

        async_vm_start.wait()
        print("VM {} has been started.".format(name))

    def stop_azure_vm(self,resource_group_name,name):
        """
        Function to stop a VM
        """
        async_vm_start = self.compute_client.virtual_machines.begin_deallocate(
            resource_group_name,
            name
        )

        async_vm_start.wait()
        print("VM {} has been stopped and deallocated.".format(name))



if __name__ == '__main__':
    # Example usage
    my_instance = AzureRM(
        client_id = os.environ.get('CLIENT_ID_CONTRIB', None),
        client_secret = os.environ.get('CLIENT_SECRET_CONTRIB', None),
        tenant_id = os.environ.get('TENANT_ID', None),
        subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
    )
    RESOURCE_GROUP_NAME = 'Koch_lab'
    VM_NAME = 'PersonalServer'
    VM_ACTION = 'Stop'  
    
    vm_size = my_instance.get_azure_vm(RESOURCE_GROUP_NAME,VM_NAME).hardware_profile.vm_size
    vm_state = my_instance.get_azure_vm_powerstate(RESOURCE_GROUP_NAME,VM_NAME)
    vm_os = my_instance.get_azure_vm(RESOURCE_GROUP_NAME,VM_NAME).storage_profile.os_disk.os_type

    print("vm_size: " + vm_size)
    print("vm_os: " + vm_os)
    print("vm_state: " + vm_state)
    if ('deallocated' in vm_state.lower()) and (VM_ACTION.lower() == 'start'):
        print("Trying to start VM")
        my_instance.start_azure_vm(RESOURCE_GROUP_NAME,VM_NAME)
    
    if ('running' in vm_state.lower()) and (VM_ACTION.lower() == "stop"):
        print("Trying to stop VM")
        my_instance.stop_azure_vm(RESOURCE_GROUP_NAME,VM_NAME)

