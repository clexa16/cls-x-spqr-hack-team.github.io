import time
import random
import sys
import os

# Tiny10 terminalinde renkleri aktif etme komutu
os.system('')

# Renk Kodları (Sadece Kırmızı ve Yeşil odaklı)
NEON_GREEN = "\033[1;92m"
NEON_RED   = "\033[1;91m"
NEON_CYAN  = "\033[1;96m"
BOLD       = "\033[1m"
RESET      = "\033[0m"
CLEAR_SCREEN = "\033[2J\033[H"

TOOLS = [
    {"name": "DDoS Attack",          "input": "Target IP"},
    {"name": "RAT Controller",       "input": "Target IP"},
    {"name": "SMS Bomber",           "input": "Phone Number"},
    {"name": "Port Scanner",         "input": "Target IP"},
    {"name": "Brute Force SSH",      "input": "Target IP"},
    {"name": "WiFi Cracker",         "input": "WiFi SSID"},
    {"name": "Phishing Page Generator", "input": "Target URL"},
    {"name": "Keylogger",            "input": "Target IP"},
    {"name": "Packet Sniffer",       "input": "Network Interface"},
    {"name": "Malware Builder",      "input": "Payload Name"},
    {"name": "Exploit Injector",     "input": "Target IP"},
    {"name": "SQL Injection",        "input": "Target URL"},
    {"name": "XSS Attack Simulator", "input": "Target URL"},
    {"name": "Credential Harvester", "input": "Email Address"},
    {"name": "DNS Spoofing",         "input": "Target Domain"},
    {"name": "ARP Spoofing",         "input": "Target IP"},
    {"name": "Session Hijacker",     "input": "Target Session ID"},
    {"name": "MAC Address Changer",  "input": "New MAC Address"},
    {"name": "HTTP Flood",           "input": "Target IP"},
    {"name": "VPN Bypass",           "input": "Target IP"},
]

def neon_print(text, color):
    print(color + BOLD + text + RESET)

def simulate_output(tool_name):
    # Bu döngü o neon yeşil ve kırmızı akışı sağlar
    for _ in range(20):
        color = NEON_GREEN if random.random() > 0.2 else NEON_RED
        timestamp = time.strftime("%H:%M:%S")
        fake_data = f"packet={random.randint(1000,9999)} latency={random.uniform(10,300):.1f}ms status={'OK' if random.random()>0.1 else 'FAIL'}"
        print(f"{color}[{timestamp}] {tool_name}: {fake_data} | By Clexa - CLxSPQR{RESET}")
        time.sleep(0.05) # Akış hızı (HD 4450 için optimize edildi)

def tool_loop(tool):
    os.system('cls')
    neon_print(f"--- {tool['name']} - By Clexa ---", NEON_RED)
    input_prompt = f"{NEON_CYAN}Enter {tool['input']}: {RESET}"
    target = input(input_prompt)
    
    neon_print(f"\n[!] CLxSPQR Team - Launching {tool['name']} against {target}\n", NEON_RED)
    time.sleep(1)
    
    try:
        while True:
            simulate_output(tool['name'])
    except KeyboardInterrupt:
        neon_print("\n[!] Connection Interrupted. Returning to menu...", NEON_CYAN)
        time.sleep(1)

def main_menu():
    while True:
        os.system('cls')
        print(f"{NEON_RED}{BOLD}==========================================")
        print(f"|        BY CLEXA - CLSxSPQR TEAM         |")
        print(f"|    SYSTEM: TINY10 | GPU: HD 4450       |")
        print(f"=========================================={RESET}")
        
        for idx, tool in enumerate(TOOLS, 1):
            print(f"{NEON_GREEN}[{idx:02d}]{RESET} {tool['name']}")
        
        print(f"\n{NEON_CYAN}Select (1-{len(TOOLS)}) or 0 to Exit: {RESET}", end="")
        choice = input()
        
        if choice == '0':
            neon_print("\nExiting... Stay in the shadows.", NEON_RED)
            sys.exit(0)
            
        if choice.isdigit() and (1 <= int(choice) <= len(TOOLS)):
            tool_loop(TOOLS[int(choice)-1])
        else:
            neon_print("Error! Invalid Selection.", NEON_RED)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        sys.exit(0)
