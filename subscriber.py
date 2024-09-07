# subscriber.py
import paho.mqtt.client as mqtt
from datetime import datetime
import json

broker = 'broker.hivemq.com'
topic = 'hotel/temperature'
threshold = 25  
data = []  
latest_data_file = "latest_data.json"  

# client connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(topic)

# Callback function to handle incoming messages
def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data.append((temperature, timestamp))

    
    if len(data) > 5:
        data.pop(0)

    print(f"Received Temperature: {temperature}°C at {timestamp}")

    # Save the latest temperature to the JSON file
    with open(latest_data_file, 'w') as f:
        json.dump({"temperature": temperature, "timestamp": timestamp}, f)

    # Check if all last 5 readings exceeded the threshold
    if all(temp[0] > threshold for temp in data):
        print(f"ALARM: Temperature has been above {threshold}°C for 5 minutes!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)

# Start the MQTT loop to listen for messages
client.loop_forever()

