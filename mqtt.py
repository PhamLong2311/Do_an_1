from paho.mqtt import client as mqtt_client
from config import broker, port, username, password, topic
import random
from datetime import datetime

class MQTTClient:
    def __init__(self):
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'
        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, port)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.subscribe(topic)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        protocol = "MQTT"
        # You can handle the received message here or pass it to another module
        print(f"Received message: {payload}")

    def publish(self, message):
        # Implement MQTT message publishing if needed
        pass
