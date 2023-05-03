#!/usr/bin/env python
"""Execute PowerShell command on azure windows VM"""
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

# Execute a PowerShell command on the VM via run command
run_command_parameters = {
    'command_id': 'RunPowerShellScript',
    'script': [
        #"'Get-Disk | Where partitionstyle -eq raw | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -Confirm:$false'"
        'get-wmiobject win32_computersystem'
    ]
}


async_run_command = compute_client.virtual_machines.begin_run_command(
    RESOURCE_GROUP_NAME,
    VM_NAME,
    run_command_parameters
)

run_command_result = async_run_command.result()

# Print the output of the PowerShell command
for run in run_command_result.value:
    print("Output of the PowerShell command on VM {}:\n {}".format(VM_NAME, run.message))

