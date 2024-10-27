import network
import time

# List of known Wi-Fi networks (SSID, Password) you can add here more networks
known_networks = [
    ("Rassi Net-2.4G", "password"),
    ("WorkWifi", "password"),
    ("FriendNet", "friendpassword")
]


def connect_to_internet():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    # Loop through each known network
    for ssid, password in known_networks:
        if not sta_if.isconnected():
            print(f'Attempting to connect to {ssid}...')
            sta_if.connect(ssid, password)
            
            # Timeout to try connecting for 12 seconds before moving to the next network
            start_time = time.time()
            while not sta_if.isconnected() and (time.time() - start_time) < 12:
                pass
            
            # Check if connected after timeout
            if sta_if.isconnected():
                print(f'Connected to {ssid} with IP:', sta_if.ifconfig()[0])
                blueled.on()  # Turn on onboard LED
                return True  # Exit function as we are connected
            
            # Disconnect if unable to connect and move to next network
            print(f'Failed to connect to {ssid}, moving to next network.')
            sta_if.disconnect()

    print("Could not connect to any known networks.")
    return False
