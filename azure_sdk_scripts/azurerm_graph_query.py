#!/usr/bin/env python
"""
Description : Module to execute graph query on azure
Version     : 1.0
Maintainer  : Vikas Pandey, <vikiscripts@gmail.com>
Date        : 04-June-2023
"""
import os
import json
import azure.identity
import azure.mgmt.resourcegraph as arg
from azure.mgmt.resource import SubscriptionClient

# Wrap all the work in a function
def getresources(query):
    '''Azure resource graph query'''
    _credential = azure.identity.ClientSecretCredential(
        tenant_id=os.environ.get("TENANT_ID", ""),
        client_id=os.environ.get("CLIENT_ID", ""),
        client_secret=os.environ.get("CLIENT_SECRET", "")
    )
    subs_client = SubscriptionClient(_credential)
    subs_raw = []
    for sub in subs_client.subscriptions.list():
        subs_raw.append(sub.as_dict())
    subs_list = []
    
    for sub in subs_raw:
        subs_list.append(sub.get('subscription_id'))

    arg_client = arg.ResourceGraphClient(_credential)
    arg_query_options = arg.models.QueryRequestOptions(result_format="objectArray")
    arg_query = arg.models.QueryRequest(subscriptions=subs_list, query=query, options=arg_query_options)
    _results = arg_client.resources(arg_query)
    
    print(_results)

getresources("Resources | project name, type | limit 5")
