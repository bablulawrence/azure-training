# Databricks notebook source
# MAGIC %run "./includes/utils"

# COMMAND ----------

dbutils.widgets.text("subject", "")
dbutils.widgets.text("fileName", "")
dbutils.widgets.text("folderPath", "/data/cleansed/green_taxi")
dbutils.widgets.text("uploadedBy", "")
cleansedFolderPath = dbutils.widgets.get("folderPath")
curatedFolderPath = "/data/curated"

# COMMAND ----------

cleansedDf = spark.read.format("delta").load("/mnt" + cleansedFolderPath)

# COMMAND ----------

from pyspark.sql.functions import sum, mean, round, lit

zoneSummaryDf = ( cleansedDf
                 .groupBy("PULocationID","DOLocationID")
                 .agg(sum("passenger_count").cast("Int").alias("total_passenger_count"),
                     round(mean("passenger_count"),2).alias('avg_passenger_count'),
                     round(mean("fare_amount"),2).alias("avg_fare_amount"),
                     round(mean("extra"),2).alias("avg_extra"),
                     round(mean("mta_tax"),2).alias("avg_mta_tax"),                     
                     round(mean("tip_amount"),2).alias("avg_tip_amount"),                      
                     round(mean("tolls_amount"),2).alias("avg_tolls_amount"),
                     round(mean("ehail_fee"),2).alias("avg_ehail_fee"),
                     round(mean("improvement_surcharge"),2).alias("avg_improvement_surcharge"),
                     round(mean("total_amount"),2).alias("avg_total_amount"),                   
                    ).withColumn("avg_congestion_surcharge", lit(0.0))
                     .withColumn("taxi_type",lit("Green"))
            )

# COMMAND ----------

# dbutils.fs.rm("/mnt" + curatedFolderPath+ "/zone_summary", recurse=True)
( zoneSummaryDf.write.format("delta")
    .mode("append")
    .save("/mnt" + curatedFolderPath+ "/fact_zone_summary")
)

# COMMAND ----------

publishEvent(eventSubject=dbutils.widgets.get("subject"), 
             eventType="NYCTaxi.GreenTaxi.TripData.ZoneSummaryCurated", 
             eventData={ "folderPath":f"{curatedFolderPath}/fact_zone_summary",
                         "fileName": dbutils.widgets.get("fileName"),
                         "uploadedBy": dbutils.widgets.get("uploadedBy")})