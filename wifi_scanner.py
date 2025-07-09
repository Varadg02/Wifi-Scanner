import pywifi
from pywifi import const
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # get the first Wi-Fi interface

    iface.scan()  # start scanning
    time.sleep(2)  # wait for scan to complete

    results = iface.scan_results()
    networks = []

    print("Available Wi-Fi Networks:")
    print("=" * 50)
    for network in results:
        ssid = network.ssid
        signal = network.signal
        auth = get_auth_type(network.akm)
        
        print(f"SSID: {ssid or 'Hidden'}")
        print(f"Signal Strength: {signal} dBm")
        print(f"Security: {auth}")
        print("-" * 50)

def get_auth_type(akm_list):
    if not akm_list:
        return "Open"
    akm_str = []
    for akm in akm_list:
        if akm == const.AKM_TYPE_NONE:
            akm_str.append("Open")
        elif akm == const.AKM_TYPE_WPA:
            akm_str.append("WPA")
        elif akm == const.AKM_TYPE_WPAPSK:
            akm_str.append("WPA-PSK")
        elif akm == const.AKM_TYPE_WPA2:
            akm_str.append("WPA2")
        elif akm == const.AKM_TYPE_WPA2PSK:
            akm_str.append("WPA2-PSK")
        else:
            akm_str.append("Unknown")
    return "/".join(akm_str)

if __name__ == "__main__":
    scan_networks()
