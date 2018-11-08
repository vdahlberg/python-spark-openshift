import os
from os import environ
from pyspark.sql import SparkSession
#from pyspark.sql.functions import mean, col

storage_account_name = "svvpocdlgen2"
storage_account_access_key = environ.get("STORAGE_KEY")


spark = SparkSession.builder.appName('wrangler').config("spark.hadoop.fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.azure.account.key."+storage_account_name+".blob.core.windows.net", storage_account_access_key).getOrCreate()
			

file_location = "abfss://testshare/"

df = spark.read.format("csv").options(header='true',inferschema='true',sep=";").load("wasbs://testshare@svvpocdlgen2.blob.core.windows.net/1900116_20180306000000-20180331235900.csv")
#df_mean = df.select(mean(col('vehicle_type_quality'))).collect()

jdbcHostname = "svvpocsql1.database.windows.net"
jdbcDatabase = "svvpocdb1"
jdbcPort = 1433
username = "svvpocadmin@svvpocsql1"
password = environ.get("SQLDB_PWD")

jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2}".format(jdbcHostname, jdbcPort, jdbcDatabase)
connectionProperties = {
  "user" : username,
  "password" : password,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

df.createOrReplaceTempView("vehicledata")

import org.apache.spark.sql.SaveMode

spark.table("vehicledata").write.mode(SaveMode.Overwrite).jdbc(jdbcUrl, "vehicledata", connectionProperties)


vehicle_type_table = spark.read.jdbc(jdbcUrl, "vehicledata", connectionProperties)
print(vehicle_type_table.select('vehicle_type_quality', 'vehicle_type').groupBy('vehicle_type').avg('vehicle_type_quality'))

spark.stop()

