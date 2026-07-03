from pyspark.sql.functions import (
    to_timestamp,
    to_date,
    year,
    month,
    col
)


def add_bronze_columns(df):
    """
    Add columns required for the Bronze Layer.

    This function:
    1. Converts event_timestamp to TimestampType.
    2. Creates event_date.
    3. Creates year and month partition columns.
    """

    df = (
        df.withColumn(
            "event_timestamp",
            to_timestamp(col("event_timestamp"))
        )
        .withColumn(
            "event_date",
            to_date(col("event_timestamp"))
        )
        .withColumn(
            "year",
            year(col("event_timestamp"))
        )
        .withColumn(
            "month",
            month(col("event_timestamp"))
        )
    )

    return df