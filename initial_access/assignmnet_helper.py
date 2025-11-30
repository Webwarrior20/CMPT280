#!/usr/bin/env python3
"""
Terminal Initial-Access Simulation

⚠ EDUCATIONAL USE ONLY ⚠
- This script is for a malware / worm simulation lab.
- Do NOT enter real MacEwan or personal credentials.
- Use only fake usernames/password-like strings inside your isolated VM.
"""

import os
import getpass
from datetime import datetime

# Directory where simulated "credentials" are stored
LOG_DIR = "/home/seed/Documents/CMPT280/Final_Project/collected"
LOG_FILE = os.path.join(LOG_DIR, "simulated_terminal_tokens.txt")
os.makedirs(LOG_DIR, exist_ok=True)

def main():
    print("=== Assignment Auto-Submit (SIMULATION) ===\n")
    print("This is a controlled lab exercise.")
    print("➡ DO NOT enter your real MacEwan email or password.")
    print("➡ Use any FAKE username and password-like string.\n")

    fake_user = input("Enter a FAKE username for the simulation: ")
    fake_secret = getpass.getpass("Enter any FAKE 'password' string (input hidden): ")

    # Save to log file as a simulated “access token”
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] USER={fake_user} SECRET={fake_secret}\n")

    print("\nSimulating connection to assignment submission server...")
    print("Simulation complete. No real login was performed.")
    print("Thank you for participating in this lab exercise.")

if __name__ == "__main__":
    main()
