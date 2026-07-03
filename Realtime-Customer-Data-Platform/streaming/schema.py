from pyspark.sql.types import *

event_schema = StructType([
    StructField("event_id", StringType()),
    StructField("user_id", IntegerType()),
    StructField("session_id", StringType()),
    StructField("event_type", StringType()),
    StructField("event_timestamp", StringType()),

    StructField("product_id", StringType()),
    StructField("product_name", StringType()),
    StructField("category", StringType()),

    StructField("price", IntegerType()),
    StructField("quantity", IntegerType()),

    StructField("country", StringType()),
    StructField("city", StringType()),

    StructField("device", StringType()),
    StructField("browser", StringType()),
    StructField("referral_source", StringType())
])