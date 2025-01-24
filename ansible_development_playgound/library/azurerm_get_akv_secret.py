#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import azure.identity
import azure.keyvault.secrets

def get_akv_secret(vault_url,secret_name,tenant_id=None,client_id=None,client_secret=None,use_msi=False):
    '''Read Azure keyvault secret'''
    if use_msi:
        credential=azure.identity.ManagedIdentityCredential()
    else:
        credential=azure.identity.ClientSecretCredential(tenant_id,client_id,client_secret)
    secret = azure.keyvault.secrets.SecretClient(
        vault_url,
        credential
    ).get_secret(secret_name).value

    return secret


def main():
    '''Main def to invoke ansible module'''
    arguments = dict(
            vault_url=dict(required=True),
            secret_name=dict(required=True),
            tenant_id=dict(required=False),
            client_id=dict(required=False),
            client_secret=dict(required=False,no_log=True),
            use_msi=dict(required=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(changed=True)

    if module.params['use_msi']:
        result['original_message'] = get_akv_secret(
            module.params['vault_url'],
            module.params['secret_name'],
            user_msi=True
        )
    else:
        result['original_message'] = get_akv_secret(
            module.params['vault_url'],
            module.params['secret_name'],
            module.params['tenant_id'],
            module.params['client_id'],
            module.params['client_secret']
        )
    
    result['message'] = 'testing azure rm scripts'

    # OUTPUT
    module.exit_json(**result)


if __name__ == '__main__':
    main()
