import os
from os import environ
from pyspark.sql import SparkSession
#import mysql.connector

#db = mysql.connector.connect(host=environ.get("MYSQL_HOST"), user=environ.get("MYSQL_USER"), passwd=environ.get("MYSQL_PWD"))

#cursor = db.cursor()
#cursor.execute("SHOW DATABASES")

#for x in cursor:
#    print(x)

storage_account_name = "svvpocdlgen2"
storage_account_access_key = environ.get("STORAGE_KEY")


spark = SparkSession.builder.appName('wrangler').config("spark.hadoop.fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.wasbs.impl", "org.apache.hadoop.fs.azure.NativeAzureFileSystem").config("fs.azure.account.key."+storage_account_name+".blob.core.windows.net", storage_account_access_key).getOrCreate()
			

file_location = "abfss://testshare/"

df = spark.read.format("csv").options(header='true',inferschema='true',sep=";").load("wasbs://testshare@svvpocdlgen2.blob.core.windows.net/1900116_20180306000000-20180331235900.csv")
print(df)
spark.stop()

