# publisher.py
import random
import time
import paho.mqtt.client as mqtt

# MQTT Broker settings
broker = 'broker.hivemq.com'  
topic = 'hotel/temperature'    

# Function to connect to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))

# Create an MQTT client instance
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, 1883, 60)  

def generate_temperature_and_publish():
    while True:
        # Generate random temperature data
        temperature = round(random.uniform(-10, 40), 2)

        # Publish the data
        client.publish(topic, temperature)
        print(f"Published Temperature: {temperature}°C to topic: {topic}")
        
        # Wait for 60 seconds
        time.sleep(60)

# Start generating and publishing temperature data
generate_temperature_and_publish()

