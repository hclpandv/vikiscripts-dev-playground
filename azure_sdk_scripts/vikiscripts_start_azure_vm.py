#!/usr/bin/env python
"""Get VM details from Azure"""
import os
import azure.identity
import azure.mgmt.compute

RESOURCE_GROUP_NAME = 'Koch_lab'
VM_NAME = 'PersonalServer'

credential = azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID_CONTRIB", ""),
        client_secret=os.environ.get("CLIENT_SECRET_CONTRIB", "")
)

compute_client = azure.mgmt.compute.ComputeManagementClient(
    credential=credential,
    subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
)


async_vm_start = compute_client.virtual_machines.begin_start(
    RESOURCE_GROUP_NAME, 
    VM_NAME
)

async_vm_start.wait()

print("VM {} has been started.".format(VM_NAME))
