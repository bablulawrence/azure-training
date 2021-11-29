# Databricks notebook source
# MAGIC %run "./includes/utils"

# COMMAND ----------

dbutils.widgets.text("subject", "")
dbutils.widgets.text("fileName", "")
dbutils.widgets.text("folderPath", "/data/raw/yellow_taxi")
dbutils.widgets.text("uploadedBy", "")
rawFolderPath = dbutils.widgets.get("folderPath")
cleansedFolderPath = "/data/cleansed/yellow_taxi"

# COMMAND ----------

from pyspark.sql.functions import col

yellowTaxiDf = ( spark.read.csv("/mnt"+ rawFolderPath, inferSchema=True, header=True)
                    .withColumn("VendorId", col("VendorId").cast("Int")).dropna(subset=["VendorId"])
              )

# COMMAND ----------

# dbutils.fs.rm(cleansedFolderPath, recurse=True)
( yellowTaxiDf.write.format('delta')
    .mode("overwrite")
    .save("/mnt" + cleansedFolderPath)
)

# COMMAND ----------

publishEvent(eventSubject=dbutils.widgets.get("subject"), 
             eventType="NYCTaxi.YellowTaxi.TripData.FileCleansed", 
             eventData={ "folderPath":cleansedFolderPath,
                         "fileName": dbutils.widgets.get("fileName"),
                         "uploadedBy": dbutils.widgets.get("uploadedBy")})