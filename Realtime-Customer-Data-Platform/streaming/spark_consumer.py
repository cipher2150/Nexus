from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from schema import event_schema
from transformations import add_bronze_columns
from writer import write_to_bronze

from config import (
    APP_NAME,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    BRONZE_PATH,
    CHECKPOINT_PATH,
)


def create_spark_session():
    """
    Create and configure the Spark session.
    """

    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master("local[*]")
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6"
        )
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark


def read_kafka_stream(spark):
    """
    Read events continuously from Kafka.
    """

    df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", KAFKA_TOPIC)
        .option("startingOffsets", "latest")
        .load()
    )
    
    parsed_df = (
        df.selectExpr("CAST(value AS STRING)")
        .select(
            from_json(col("value"), event_schema).alias("data")
        )
        .select("data.*")
    )
    
    bronze_df = add_bronze_columns(parsed_df)

    bronze_df.printSchema()

    query = write_to_bronze(
        bronze_df,
        BRONZE_PATH,
        CHECKPOINT_PATH
    )

    query.awaitTermination()


if __name__ == "__main__":

    spark = create_spark_session()

    read_kafka_stream(spark)