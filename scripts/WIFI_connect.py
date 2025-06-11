import network
import time


def connect_wifi(ssid, password):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    
    wlan = network.WLAN(network.STA_IF)
    
    if not wlan.active():
        wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)

        MAX_attempt = 30
        attempt_count = 0
        
        while not wlan.isconnected() and attempt_count < MAX_attempt:
            attempt_count += 1
            time.sleep(0.4)
        
        if wlan.isconnected():
            print('Successfully connected')
            return True
        else:
            print('Could not connect to the WiFi network')
            return False
    else:
        print('Already connected to network')
        return True



        