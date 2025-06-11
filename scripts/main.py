import WIFI_connect
import mqtt
import time

###DO NOT USE THIS CODE YET, OTHER CODES NEEDS TO BE MADE BEFORE THIS IS RAN


# WiFi and Adafruit IO details
WIFI_SSID = 'HOTSPOT SSID'
WIFI_PASSWORD = 'HOTSPOT PASSWORD'

AIO_USERNAME = 'AIO USERNAME'
AIO_KEY = 'AIO KEY'

# Feeds
TEMP_FEED = AIO_USERNAME + '/feeds/temperature'
OD_FEED = AIO_USERNAME + '/feeds/od'
PID_FEED = AIO_USERNAME + '/feeds/pid'


# Connecting to the wifi
connection = WIFI_connect.connect_wifi(WIFI_SSID, WIFI_PASSWORD)


if not connection:
    print("Wi-Fi connection failed. Cannot proceed.")
else:
    print("Wi-Fi connected. Proceeding to MQTT...")
    # Connecting to Adrafruit IO
    client = mqtt.setup_mqtt(AIO_USERNAME, AIO_KEY)

    while True:
        # Test Data, needs to be changed
        temperature = 1
        od_value = 2
        pid_output = 3

        # Publish to Adafruit IO
        client.publish(TEMP_FEED, str(temperature))
        client.publish(OD_FEED, str(od_value))
        client.publish(PID_FEED, str(pid_output))
        print('Published data:', temperature, od_value, pid_output)

        time.sleep(2)