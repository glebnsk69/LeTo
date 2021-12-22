import network
from time import sleep

def do_connect():
    print("========== Start BOOT ===========")
    ssid = "0370-mobile"
    password = "Vfhn2007"

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to network")
        wlan.connect(ssid, password)
        sleep(3)
        while not wlan.isconnected:
            pass
    print("Connection successful",wlan.ifconfig())


do_connect()
