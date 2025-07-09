# 📡 Wi-Fi Network Scanner (Python)

## 📝 Description
This is a simple Python script that scans for nearby Wi-Fi networks and displays their details including:

- 📶 SSID (Wi-Fi name)
- 📉 Signal strength (in dBm)
- 🔒 Security type (WPA/WPA2/Open)

This tool is helpful for users to choose the best Wi-Fi network based on signal strength and security.

---

## 🚀 Features
- Scans all available nearby Wi-Fi networks
- Displays SSID (or "Hidden" if not broadcasted)
- Shows signal strength
- Detects authentication/security type (WPA, WPA2, Open, etc.)

---

## 🛠 Requirements

- Python 3.x
- `pywifi` library

Install dependencies with:

```bash
pip install pywifi
💻 How to Run
Ensure your device has an active Wi-Fi adapter (and it's enabled).

Download or clone this repository.

Save the script as wifi_scanner.py.

Run the script:

bash
Copy
Edit
python wifi_scanner.py
🧪 Sample Output
yaml
Copy
Edit
Available Wi-Fi Networks:
==================================================
SSID: Home_Network
Signal Strength: -45 dBm
Security: WPA2-PSK
--------------------------------------------------
SSID: CollegeWiFi
Signal Strength: -68 dBm
Security: WPA/WPA2
--------------------------------------------------
SSID: Hidden
Signal Strength: -80 dBm
Security: Open
--------------------------------------------------
❗ Notes
This script is tested on Windows.

On some machines, scanning may take 2–5 seconds — do not interrupt it.

If pywifi shows no interfaces, try running the script as Administrator.

⚙️ Platform Compatibility
OS	Supported	Notes
Windows	✅ Yes	Fully tested and supported
Linux	⚠️ Partial	pywifi may not work on all systems
macOS	❌ No	pywifi not supported on macOS
