# Databricks notebook source
# MAGIC %run "./includes/utils"

# COMMAND ----------

dbutils.widgets.text("subject", "")
dbutils.widgets.text("fileName", "")
dbutils.widgets.text("folderPath", "/data/raw/green_taxi")
dbutils.widgets.text("uploadedBy", "")
rawFolderPath = dbutils.widgets.get("folderPath")
cleansedFolderPath = "/data/cleansed/green_taxi"

# COMMAND ----------

from pyspark.sql.functions import col

greenTaxiDf = ( spark.read.csv("/mnt"+ rawFolderPath, inferSchema=True, header=True)
                    .withColumn("VendorId", col("VendorId").cast("Int")).dropna(subset=["VendorId"])
                    .withColumn("PULocationID", col("PULocationID").cast("Int"))
                    .withColumn("DOLocationID", col("DOLocationID").cast("Int"))
              )

# COMMAND ----------

# dbutils.fs.rm("/mnt" + cleansedFolderPath, recurse=True)
( greenTaxiDf.write.format('delta')
    .mode("overwrite")
    .save("/mnt" + cleansedFolderPath)
)

# COMMAND ----------

publishEvent(eventSubject=dbutils.widgets.get("subject"), 
             eventType="NYCTaxi.GreenTaxi.TripData.FileCleansed", 
             eventData={ "folderPath":cleansedFolderPath,
                         "fileName": dbutils.widgets.get("fileName"),
                         "uploadedBy": dbutils.widgets.get("uploadedBy")})