# Databricks notebook source
# MAGIC %run ./includes/utils

# COMMAND ----------

mountDataLake(clientId="64492359-3450-4f1e-be01-8717789fd01e", 
              clientSecret=dbutils.secrets.get(scope="dpdatalake",key="adappsecret"),
              tokenEndPoint="https://login.microsoftonline.com/0b55e01a-573a-4060-b656-d1a3d5815791/oauth2/token",
              storageAccountName="dpdatalake",
              containerName="data")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS nyctaxi;
# MAGIC USE nyctaxi;
# MAGIC CREATE TABLE IF NOT EXISTS fact_zone_summary
# MAGIC   USING DELTA
# MAGIC   LOCATION '/mnt/data/curated/fact_zone_summary';
# MAGIC CREATE TABLE IF NOT EXISTS dim_zone_lookup
# MAGIC   USING DELTA
# MAGIC   LOCATION '/mnt/data/curated/dim_zone_lookup';