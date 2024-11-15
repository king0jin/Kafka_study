import sys
import six
if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaConsumer
import json

class MessageConsumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.consumer = KafkaConsumer(
            topic, # Topic to consume
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode("utf-8"), # Decode message value as utf-8
            group_id="my-group", # Consumer group ID
            auto_offset_reset="earliest", # Start consuming from earliest available message
            enable_auto_commit=True, # Commit offsets automatically
        )

    def receive_message(self):
        try:
            for message in self.consumer:
                try:
                    result = json.loads(message.value)  # Parse message to JSON
                    for k, v in result.items():
                        print(f"{k}: {v}")
                    
                    # Print specific fields if they exist
                    # print("Name:", result.get("name", "N/A"))
                    # print("Age:", result.get("age", "N/A"))
                    
                except json.JSONDecodeError:
                    print("Received a non-JSON message:", message.value)
                    
        except Exception as exc:
            print("An error occurred while receiving messages:", str(exc))

# 브로커와 토픽명을 지정한다.
broker = ["localhost:9092"]
topic = "exam-topic"
cs = MessageConsumer(broker, topic)
cs.receive_message()
