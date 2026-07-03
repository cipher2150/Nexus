from pyspark.sql.streaming import StreamingQuery


def write_to_bronze(df, output_path, checkpoint_path) -> StreamingQuery:
    """
    Write streaming dataframe into Bronze layer
    using Parquet format.
    """

    query = (
        df.writeStream
        .format("parquet")
        .outputMode("append")
        .option("path", output_path)
        .option("checkpointLocation", checkpoint_path)
        .partitionBy(
            "year",
            "month"
        )
        .start()
    )

    return query