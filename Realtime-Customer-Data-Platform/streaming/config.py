# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092" # Kafka broker address
KAFKA_TOPIC = "customer-events" # Topic spark will read from

# Spark Application
APP_NAME = "ClickstreamStreaming" # Name shown in Spark UI

# Output Paths
BRONZE_PATH = "./bronze" # folder where raw events will be stored

# Checkpoint Location
CHECKPOINT_PATH = "./checkpoints/bronze" #Sores spark progress so it can recover after failure