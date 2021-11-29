# Databricks notebook source
from pyspark.sql.functions import count
spark.read.load("/mnt/data/curated/zone_summary").groupBy("taxi_type").agg(count("taxi_type")).show()

# COMMAND ----------

spark.read.load("/mnt/data/curated/dim_zone_lookup").printSchema()

# COMMAND ----------

spark.read.load("/mnt/data/curated/fact_zone_summary").show()

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS NycTaxi")

# COMMAND ----------

spark.sql("USE NycTaxi")
spark.sql("""CREATE TABLE fact_zone_summary 
            USING DELTA
            LOCATION '/mnt/data/curated/fact_zone_summary'""")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM fact_zone_summary

# COMMAND ----------

spark.sql("""CREATE TABLE dim_zone_lookup
            USING DELTA
            LOCATION '/mnt/data/curated/dim_zone_lookup'""")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW Tables

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * FROM fact_zone_summary

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC SELECT * FROM dim_zone_lookup

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  zone as Zone, borough as Borough, taxi_type TaxiType, total_passenger_count as `Total Passengers`, avg_total_amount as `Average Fare`  FROM 
# MAGIC fact_zone_summary as F JOIN dim_zone_lookup as D
# MAGIC ON F.PULocationID = D.location_id
# MAGIC WHERE taxi_type = 'Yellow'
# MAGIC ORDER BY total_passenger_count DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE dimzonelookup