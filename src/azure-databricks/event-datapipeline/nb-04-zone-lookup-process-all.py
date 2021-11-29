# Databricks notebook source
url = "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
from pyspark import SparkFiles
spark.sparkContext.addFile(url)

zoneLookUpDf = spark.read.csv(f"file://{SparkFiles.get('taxi+_zone_lookup.csv')}", header=True, inferSchema= True)
( zoneLookUpDf.write.format("csv")
     .option("header", True)
     .mode("overwrite")
     .save("/mnt/data/raw/zone_lookup")
)

# COMMAND ----------

( spark.read.csv("/mnt/data/raw/zone_lookup", header=True, inferSchema= True)
        .withColumnRenamed("LocationId", "location_id")
        .withColumnRenamed("Borough", "borough")
        .withColumnRenamed("Zone", "zone")
        .write.format("delta")
        .mode("overwrite")
        .save("/mnt/data/cleansed/zone_lookup")
)

# COMMAND ----------

( spark.read.load("/mnt/data/cleansed/zone_lookup")
      .write.format("delta")
      .mode("overwrite")
      .save("/mnt/data/curated/dim_zone_lookup")
)