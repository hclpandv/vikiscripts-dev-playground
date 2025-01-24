# information needed to send data to the DCR endpoint
endpoint_uri = "https://dce01-dt11.westeurope-1.ingest.monitor.azure.com" # logs ingestion endpoint of the DCR
dcr_immutableid = "dcr-3fbaf3b21cb54db99648616fa4ce402c" # immutableId property of the Data Collection Rule
stream_name = "Custom-AScertificateExpiring_CL" #name of the stream in the DCR that represents the destination table

# Import required modules
import os
import dotenv
import datetime
from azure.identity import ClientSecretCredential
from azure.monitor.ingestion import LogsIngestionClient
from azure.core.exceptions import HttpResponseError

# Load environment vars from .env file
dotenv.load_dotenv()

TENANT_ID = os.environ.get("TENANT_ID")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

credential = ClientSecretCredential(tenant_id=TENANT_ID,client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
client = LogsIngestionClient(endpoint=endpoint_uri, credential=credential, logging_enable=True)
threshold_days = 29
expired_certificates = [
    "cert_1",
    "cert_2"
]

body = [{
        "TimeGenerated": "2023-03-15T15:04:48.423211Z",
        "ExpiryDetails": f"Certificates are expiring in less than {threshold_days} days",
        "ExpiringCertificates": expired_certificates,
        "Severitylevel": "High" if expired_certificates else "Low"
}]


try:
    client.upload(rule_id=dcr_immutableid, stream_name=stream_name, logs=body)
except HttpResponseError as e:
    print(f"Upload failed: {e}")
