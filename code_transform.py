configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "client id",
"fs.azure.account.oauth2.client.secret": 'secret key',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/tenantid/oauth2/token"}

dbutils.fs.mount(
source = "abfss://healthandfitnessdata@healthandfitnessdata.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/healthdata",
extra_configs = configs)

spark

dailyactivitymerged = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/dailyactivitymerged.csv")
dailycalories = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/dailycalories.csv")
dailyIntensitie = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/dailyIntensitie.csv")
dailystep = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/dailystep.csv")
hourlycalories = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/hourlycalories.csv")
hourlyintensities = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/hourlyintensities.csv")
hourlysteps = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/hourlysteps.csv")
minuteCaloriesWide = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/minuteCaloriesWide.csv")
minuteIntensitiesWide = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/minuteIntensitiesWide.csv")
minuteSleep = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/minuteSleep.csv")
minuteStepsWide = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/minuteStepsWide.csv")
sleepDay = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/sleepDay.csv")
weightLogInfo = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/healthdata/raw-data/weightLogInfo.csv")


dailyactivitymerged.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/dailyactivitymerged")
dailycalories.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/dailycalories")
dailyIntensitie.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/dailyIntensitie")
dailystep.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/dailystep")
hourlycalories.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/hourlycalories")
hourlyintensities.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/hourlyintensities")
hourlysteps.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/hourlysteps")
minuteCaloriesWide.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/minuteCaloriesWide")
minuteIntensitiesWide.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/minuteIntensitiesWide")
minuteSleep.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/minuteSleep")
minuteStepsWide.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/minuteStepsWide")
sleepDay.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/sleepDay")
weightLogInfo.repartition(1).write.mode("overwrite").option("header",'true').csv("/mnt/healthdata/transform-data/weightLogInfo")
