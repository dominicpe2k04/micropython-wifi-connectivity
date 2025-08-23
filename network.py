import network
import socket
import time

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

ssid = 'Common'
password = 'password'

def open_socket():
    adress = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(adress)
    s.listen(3)
    return(s)


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
    
    if wifi.isconnected():
        try:
            s = open_socket()
            client = s.accept()[0]
            request = client.recv(1024)
            request = str(request)
            print(request)
        except OSError as e:
            print("error")
#         
    time.sleep(1)