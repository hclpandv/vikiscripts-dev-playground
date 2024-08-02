#!/usr/bin/env python3

import os
from datetime import datetime, timezone, timedelta
from azure.identity import ManagedIdentityCredential
from azure.keyvault.certificates import CertificateClient
from azure.communication.email import EmailClient
from azure.core.exceptions import AzureError
from automationassets import get_automation_variable, AutomationAssetNotFound

# Configuration constants
SUBSCRIPTION_ID = "b4bd79bb-2081-4f1e-8cc4-5c600d3bafc2"
VAULT_URL = "https://vikivault01.vault.azure.net/"
RECIPIENTS = [
    {"address": "vikas.pandey@mixymix.com", "displayName": "Vikas Pandey"},
    {"address": "vikiscripts@gmail.com", "displayName": "Vikas Pandey"}
]
SENDER_ADDRESS = "DoNotReply@6545a451-9d70-4f84-886e-937d4ae193c7.azurecomm.net"
EXPIRY_THRESHOLD_DAYS = 50

# read email secrets from automation accounts variables
try:
    EMAIL_ENDPOINT = get_automation_variable("azure_email_endpoint")
    EMAIL_ACCESS_KEY = get_automation_variable("azure_email_access_key")
except AutomationAssetNotFound:
    print ("variable(s) not found. Please check in Automation account shared variables settings")

def get_certificate_expiry_status(vault_url, credential):
    try:
        certificate_client = CertificateClient(vault_url=vault_url, credential=credential)
        certificates = certificate_client.list_properties_of_certificates()
    except AzureError as e:
        print(f"Error: Failed to list certificates: {e}")
        return []

    expired_certificates = []
    now = datetime.now(timezone.utc)

    for certificate in certificates:
        certificate_name = certificate.name
        certificate_expiry = certificate.expires_on

        if not certificate_expiry:
            print(f"Warning: Certificate {certificate_name} does not have an expiry date.")
            continue

        difference = certificate_expiry - now
        if difference.days < EXPIRY_THRESHOLD_DAYS:
            expiry_date_str = certificate_expiry.date().isoformat()
            expired_certificates.append(f"Certificate {certificate_name} expires on {expiry_date_str}")
            print(f"Info: Certificate {certificate_name} is expiring soon: {expiry_date_str}")

    return expired_certificates

def send_email_alert(expired_certificates, email_client):
    if not expired_certificates:
        print("Info: No certificates are about to expire.")
        return

    expired_certificates_string = "Attention the following certificates are about to expire:\n\n" + "\n".join(expired_certificates)
    message = {
        "content": {
            "subject": "Attention: Some public certificates are about to expire in Azure keyvault vikivault01",
            "plainText": expired_certificates_string,
        },
        "recipients": {
            "to": RECIPIENTS
        },
        "senderAddress": SENDER_ADDRESS
    }

    try:
        poller = email_client.begin_send(message)
        poller.result()
        print("Info: Email alert sent successfully.")
    except AzureError as e:
        print(f"Error: Failed to send email alert: {e}")

def main():
    credential = ManagedIdentityCredential()
    expired_certificates = get_certificate_expiry_status(VAULT_URL, credential)

    email_client = EmailClient.from_connection_string(f"endpoint={EMAIL_ENDPOINT};accesskey={EMAIL_ACCESS_KEY}")
    send_email_alert(expired_certificates, email_client)

if __name__ == "__main__":
    main()
