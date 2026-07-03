from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Read Bronze")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet("../bronze")

print("\nSchema:\n")
df.printSchema()

print("\nSample Data:\n")

df.show(10, truncate=False)

spark.stop()