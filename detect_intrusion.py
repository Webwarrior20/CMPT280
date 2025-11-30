#!/usr/bin/env python3
"""
Intrusion Detection System (proposal requirement):
- Monitors each victim directory
- Detects worm actions (fake files, replica, tamper)
- Logs events
"""

import time
from pathlib import Path
from datetime import datetime

VICTIMS = [
    p for p in Path(".").resolve().glob("victim*")
    if p.is_dir()
]

EVENT_LOG = Path("intrusion_events.log")

def log(msg):
    ts = datetime.now().isoformat()
    line = f"{ts} | {msg}\n"
    print(line, end="")
    with open(EVENT_LOG, "a") as f:
        f.write(line)

def scan_victim(v):
    """Detect abnormal files or activity."""

    indicators = [
        "replica_marker.txt",
        ".shutdown",
        ".trash_demo_backup",
        "manifest.log",
        "system32.dll.fake",
        "submission_v2.py.bak",
    ]

    for item in indicators:
        path = list(v.rglob(item))
        for p in path:
            log(f"[detected] {p}")

def main():
    log("[IDS] Intrusion detection started.")

    while True:
        for v in VICTIMS:
            scan_victim(v)
        time.sleep(3)

if __name__ == "__main__":
    main()
