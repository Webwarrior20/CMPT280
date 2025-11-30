#!/usr/bin/env python3
"""
Initial Access Simulation Module
--------------------------------
This script simulates how malware might acquire fake authentication
tokens before executing the worm. It DOES NOT collect real passwords.
Only safe placeholders are allowed.
"""

import os
from datetime import datetime

# Local harmless storage location inside your project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "../collected")
LOG_FILE = os.path.join(LOG_DIR, "simulated_access_tokens.txt")

os.makedirs(LOG_DIR, exist_ok=True)

def main():
    print("=== Initial Access Simulation ===")
    print("THIS IS NOT A REAL LOGIN!")
    print("This demo asks for fake credentials ONLY.\n")

    user = input("Enter a fake username: ")
    token = input("Enter a fake access token: ")

    # store non-sensitive simulation tokens
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] USER={user} TOKEN={token}\n")

    print("\nSimulated access token captured safely.")
    print("Continuing to infection stage...\n")

if __name__ == "__main__":
    main()
