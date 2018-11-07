import os
from os import environ
from pyspark.sql import SparkSession
#import mysql.connector
#from azure.common.credentials import ServicePrincipalCredentials
#from azure.datalake.store import core, lib, multithread

#db = mysql.connector.connect(host=environ.get("MYSQL_HOST"), user=environ.get("MYSQL_USER"), passwd=environ.get("MYSQL_PWD"))

#cursor = db.cursor()
#cursor.execute("SHOW DATABASES")

#for x in cursor:
#    print(x)

spark = SparkSession.builder.appName('wrangler').getOrCreate()
#r = spark.sparkContext.parallelize(range(10))
storage_account_name = "svvpocdlgen2"
storage_account_access_key = environ.get("STORAGE_KEY")

file_location = "abfss://testshare/"
spark.conf.set("fs.azure", "org.apache.hadoop.fs.azure.NativeAzureFileSystem")
print(storage_account_access_key)
spark.conf.set("fs.azure.account.key."+storage_account_name+".blob.core.windows.net", storage_account_access_key)
df = spark.read.format("csv").options(header='true',inferschema='true',sep=";").load("wasbs://testshare@svvpocdlgen2.blob.core.windows.net/1900116_20180306000000-20180331235900.csv")
print(df)
spark.stop()
#r = r.map(lambda x: x * 2)
#r.collect()

#auth
#token = lib.auth(tenant_id = environ.get("AZ_TENANT_ID"), client_secret = environ.get("AZ_CLIENT_SECRET"), client_id = environ.get("AZ_CLIENT_ID"))

# create ADLS file system client

#adls = core.AzureDLFileSystem(token, store_name = environ.get("AZ_STORE_NAME"))
