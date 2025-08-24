import network
import socket
import time

wifi.active(False)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

ssid = 'your wifi name'
password = 'your wifi password'

while True:
    # Wifi Connection code
    if wifi.isconnected():
        print("Wi-Fi is connected:", wifi.ifconfig()[0])
    else:
        print("Lost connection! Attempting to reconnect...")
        wifi.connect(ssid, password)
        time.sleep(3)
        if wifi.isconnected():
            print("Wi-Fi is connected:", wifi.ifconfig()[0])
    # Wifi code over
    
    time.sleep(1)
