import os
from os import environ
from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, col

storage_account_name = "svvpocdlgen2"
storage_account_access_key = environ.get("STORAGE_KEY")


spark = SparkSession.builder.appName('wrangler').config("spark.hadoop.fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.azure.account.key."+storage_account_name+".blob.core.windows.net", storage_account_access_key).getOrCreate()
			

file_location = "abfss://testshare/"

df = spark.read.format("csv").options(header='true',inferschema='true',sep=";").load("wasbs://testshare@svvpocdlgen2.blob.core.windows.net/1900116_20180306000000-20180331235900.csv")
df_mean = df.select(mean(col('vehicle_type_quality'))).collect()
print(df_mean)


#jdbcHostname = "svvpocsql1.database.windows.net"
#jdbcDatabase = "svvpocdb1"
#jdbcPort = 1433
#username = "svvpocadmin@svvpocsql1"
#password = environ.get("SQLDB_PWD")
#jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2};user={3};password={4}".format(jdbcHostname, jdbcPort, jdbcDatabase, username, password)


spark.stop()

