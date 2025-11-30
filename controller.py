#!/usr/bin/env python3

"""
Controller for the simulated worm, as described in the proposal.

It signals the malware component through shared command files.
Controller does NOT run inside the container.
"""

from pathlib import Path
import sys

COMMAND_DIR = Path("./commands").resolve()
CMD = COMMAND_DIR / "command.txt"
STATUS = COMMAND_DIR / "status.txt"

def ensure_dir():
    COMMAND_DIR.mkdir(parents=True, exist_ok=True)

def send(cmd: str):
    ensure_dir()
    CMD.write_text(cmd.strip().upper() + "\n", encoding="utf-8")
    print(f"[controller] command sent: {cmd.upper()}")

def read_status():
    if not STATUS.exists():
        print("[controller] no status available yet.")
        return
    print("=== STATUS ===")
    print(STATUS.read_text())

def clear():
    for f in (CMD, STATUS):
        if f.exists():
            f.unlink()
    print("[controller] cleared command and status files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: controller.py [attack|restore|status|clear]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "attack":
        send("ATTACK")

    elif action == "restore":
        send("RESTORE")

    elif action == "status":
        read_status()

    elif action == "clear":
        clear()

    else:
        print("Unknown command. Use: attack | restore | status | clear")
