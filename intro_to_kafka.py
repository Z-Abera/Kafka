# Run both commands in the terminal inside you Kafka folder
# Remember to start Zookeeper first as it orchestrates Kafka Brokers
# Starting Zookeeper

# Starting Kafka
#./bin/kafka-server-start.sh ./config/server.properties

# Starting Zookeeper
#./bin/zookeeper-server-start.sh ./config/zookeeper.properties
from kafka import KafkaClient
from kafka.cluster import ClusterMetadata

# Create a connection to retrieve metadata
meta_cluster_conn = ClusterMetadata(
    bootstrap_servers="localhost:9092", # Specific the broker address to connect to
)

# retrieve metadata about the cluster
print(meta_cluster_conn.brokers())


# Create a connection to our KafkaBroker to check if it is running
client_conn = KafkaClient(
    bootstrap_servers="localhost:9092", # Specific the broker address to connect to
    client_id="Broker test" # Create an id from this client for reference
)

# Check that the server is connected and running
print(client_conn.bootstrap_connected())
# Check our Kafka version number
print(client_conn.check_version())
