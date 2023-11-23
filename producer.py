from kafka import KafkaProducer
from json import dumps

# Configure our producer which will send data to  the MLdata topic
ml_producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    client_id="ML data producer",
    value_serializer=lambda mlmessage: dumps(mlmessage).encode("ascii")
) 

# Configure our producer which will send data to the Retaildata topic
retail_producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    client_id="Retaild data producer",
    value_serializer=lambda retailmessage: dumps(retailmessage).encode("ascii")
)
# Lets create some test data to send using our kafka producer
ml_models = [
    {
        "Model_name": "ResNet-50",
        "Accuracy": "92.1",
        "Framework_used": "Pytorch"
    },
    {
        "Model_name": "Random Forest",
        "Accuracy": "82.7",
        "Framework_used": "SKLearn"
    }
] 

retail_data = [
    {
        "Item": "42 LCD TV",
        "Price": "209.99",
        "Quantity": "1"
    },
    {
        "Item": "Large Sofa",
        "Price": "259.99",
        "Quantity": 2
    }
]

# Send our ml data to the MLData topic
for mlmessage in ml_models:
    print("code has been executed 1")
    ml_producer.send(topic="MLdata", value=mlmessage)
    print("code has been executed")
    ml_producer.flush()

# Send retail data to the Retaildata topic
for retail_message in retail_data:
    retail_producer.send(topic="Retaildata", value=retail_message)
    print("code has been executed")
    retail_producer.flush()