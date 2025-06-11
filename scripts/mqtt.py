from umqtt.simple import MQTTClient
import ubinascii
import machine
import WIFI_connect

def setup_mqtt(username, key, server='io.adafruit.com', port=1883):
    client_id = ubinascii.hexlify(machine.unique_id())
    client = MQTTClient(client_id, server, port, username, key)
    client.connect()
    print('Connected to Adafruit IO MQTT')
    return client
