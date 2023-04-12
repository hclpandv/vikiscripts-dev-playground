#!/usr/bin/env python
"""Get VM details from Azure"""
import os
import azure.identity
import azure.mgmt.compute

RESOURCE_GROUP_NAME = 'Koch_lab'
VM_NAME = 'PersonalServerLinux'

credential = azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
)

compute_client = azure.mgmt.compute.ComputeManagementClient(
    credential=credential,
    subscription_id = os.environ.get('SUBSCRIPTION_ID', None)
)

vm = compute_client.virtual_machines.get(
    resource_group_name = RESOURCE_GROUP_NAME,
    vm_name = VM_NAME
)

print(vm)
