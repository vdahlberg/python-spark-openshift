#import os
#from os import environ
from pyspark.sql import SparkSession

#from azure.common.credentials import ServicePrincipalCredentials
#from azure.datalake.store import core, lib, multithread


spark = SparkSession.builder.appName('wrangler').getOrCreate()
r = spark.sparkContext.parallelize(range(10))
spark.stop()
r = r.map(lambda x: x * 2)
r.collect()

#auth
#token = lib.auth(tenant_id = environ.get("AZ_TENANT_ID"), client_secret = environ.get("AZ_CLIENT_SECRET"), client_id = environ.get("AZ_CLIENT_ID"))

# create ADLS file system client

#adls = core.AzureDLFileSystem(token, store_name = environ.get("AZ_STORE_NAME"))
