from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from schema import event_schema

from config import (
    APP_NAME,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
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

    # return parsed_df
    parsed_df.printSchema()
    
    query = (
        parsed_df.writeStream
        .format("console")
        .outputMode("append")
        .option("truncate", False)
        .option("numRows", 20)
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":

    spark = create_spark_session()

    read_kafka_stream(spark)