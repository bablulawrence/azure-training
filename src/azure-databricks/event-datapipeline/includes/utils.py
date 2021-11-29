# Databricks notebook source
import json
from datetime import datetime
import uuid
import requests


def mountDataLake(clientId, clientSecret, tokenEndPoint, storageAccountName, containerName):
    mountPoint = f"/mnt/{containerName}"
    if all(mount.mountPoint != mountPoint for mount in dbutils.fs.mounts()):
        configs = {"fs.azure.account.auth.type": "OAuth",
                   "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
                   "fs.azure.account.oauth2.client.id": clientId,
                   "fs.azure.account.oauth2.client.secret": clientSecret,
                   "fs.azure.account.oauth2.client.endpoint": tokenEndPoint}
        dbutils.fs.mount(
            source=f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/",
            mount_point=f"/mnt/{containerName}",
            extra_configs=configs)

# COMMAND ----------


url = "https://eg-nyctaxi.eastus2-1.eventgrid.azure.net/api/events"
key = "<enter event grid key>"


def publishEvent(eventSubject, eventType, eventData, eventGridUrl=url, eventGridKey=key):
    headers = {"aeg-sas-key": eventGridKey}
    event = [{
        "id": str(uuid.uuid4()),
        "subject": eventSubject,
        "eventType": eventType,
        "data": eventData,
        "dataVersion": 1,
        "eventTime": str(datetime.utcnow())
    }]
    return requests.post(eventGridUrl, headers=headers, data=json.dumps(event)).text
