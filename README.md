# IoT Temperature Monitoring Solution

This project simulates an IoT device that reads temperature data from a sensor and publishes it to an MQTT broker. The subscriber receives the data, raises an alarm if the temperature exceeds a threshold for 5 consecutive minutes, and stores the data locally. The server exposes the latest sensor data through an HTTP API.

## Components
1. **Publisher Program**: Publishes temperature data to an MQTT broker every 60 seconds.
2. **Subscriber Program**: Receives data, stores it locally, and raises an alarm if necessary.
3. **Server Program**: Exposes the latest sensor data via an HTTP API.

## Prerequisites
- Python 3.x
- `paho-mqtt`
- `Flask`

## Installation
1. Clone this repository:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Configuration
Make sure to configure the MQTT broker settings in both `publisher.py` and `subscriber.py` scripts if necessary.

## Usage

### 1. Running the Publisher
This publishes temperature data every 60 seconds.
```bash
python3 publisher.py
```
### 2. Running the Subsciber
This listens the temperature data and raises an alarm if necessary
```bash
python3 subscriber.py
```
### 3. Running the Flask Server
This serves the latest sensor data via an HTTP API:
```bash
python3 server.py
```
## Access the Sensor Data
Open the following URL in your browser to see latest data:
```bash
http://localhost:5000/sensor-data
```

## Customization
1. **Threshold Temperature**:You can modify the threshold temperature for an alarm in the subscriber.py script.

2. **Publish Interval**: The interval at which temperature data is published can be adjusted in publisher.py
