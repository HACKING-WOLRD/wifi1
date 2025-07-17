import os
import time

# Color Codes
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'

def banner():
    os.system('clear')
    print(f"""{G}
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║███████╗██║
██║███╗██║██║╚════██║╚═╝
╚███╔███╔╝██║███████║██╗
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝
{Y}WiFi Password Hacker (Root Check)
   {C}HACKING WORLD™ - VIP TOOL
""")

def check_root():
    return os.geteuid() == 0

def loading(text, t=3):
    for i in range(t):
        print(f"{Y}{text}{'.' * (i % 4)}", end='\r')
        time.sleep(1)

def main_tool():
    ssid = input(f"{C}Enter WiFi SSID (Name): {W}")
    print()
    loading("🔎 Scanning Network", 3)
    print(f"{G}✓ Target Found: {ssid}")
    time.sleep(1)
    print(f"{C}Signal Strength: -47 dBm | Security: WPA2/WPS")
    time.sleep(1)

    loading("📡 Attacking WPS Protocol", 4)
    print(f"{Y}• Trying pin: 87432619")
    time.sleep(1)
    print(f"{Y}• Trying pin: 45632109")
    time.sleep(1)
    print(f"{Y}• Trying pin: 19827364")
    time.sleep(1)
    print(f"{G}✓ WPS PIN Matched!")
    time.sleep(1.5)

    fake_pass = "wifi@hacked123"
    print(f"\n{R}★ Cracked Password: {W}{fake_pass}")
    print(f"{G}Connected to {ssid} successfully!")

    input(f"\n{Y}Press Enter to Exit...")

def main():
    banner()
    print(f"{C}Checking for Root Access...\n")
    time.sleep(1)

    if not check_root():
        print(f"{R}[✘] Root Access Not Found!")
        print(f"{Y}[!] This tool requires ROOT access to continue.\n")
        input(f"{W}Press Enter to Exit...")
        exit()

    print(f"{G}[✓] Root Access Detected!\n")
    time.sleep(1)
    main_tool()

main()