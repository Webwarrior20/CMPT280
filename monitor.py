#!/usr/bin/env python3
import os, time
from datetime import datetime
from pathlib import Path
import curses

TARGET_DIR = Path("./victim/assignments").resolve()
TRASH_DIR = TARGET_DIR / ".trash_demo_backup"
LOGFILE = TARGET_DIR / ".simworm_log.txt"
REPLICA_NAME = "replica_marker.txt"

FAKE_FILE_NAMES = {
    "results.tmp",
    "cache.bak",
    "system32.dll.fake",
    "report_copy.docx.fake",
    "submission_v2.py.bak",
}

def scan_stats():
    total = fake = tampered = replica = backups = 0

    for root, _, files in os.walk(TARGET_DIR):
        for f in files:
            total += 1
            path = Path(root) / f
            
            if f in FAKE_FILE_NAMES:
                fake += 1
            
            if f == REPLICA_NAME:
                replica += 1
            
            try:
                if "# TAMPER_COMMENT:" in path.read_text(errors="ignore"):
                    tampered += 1
            except:
                pass
    
    if TRASH_DIR.exists():
        backups = len(list(TRASH_DIR.iterdir()))

    return total, tampered, fake, replica, backups


def log_tail(n=10):
    if not LOGFILE.exists():
        return ["(no logs yet)"]
    lines = LOGFILE.read_text(errors="ignore").splitlines()
    return lines[-n:]


def curses_ui(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    while True:
        total, tampered, fake, replica, backups = scan_stats()
        logs = log_tail()

        stdscr.clear()
        stdscr.addstr(1, 2, f"WORM MONITOR — {datetime.now().strftime('%H:%M:%S')}")
        stdscr.addstr(3, 2, f"Total Files: {total}")
        stdscr.addstr(4, 2, f"Tampered Files: {tampered}")
        stdscr.addstr(5, 2, f"Fake Files: {fake}")
        stdscr.addstr(6, 2, f"Replica Files: {replica}")
        stdscr.addstr(7, 2, f"Backups: {backups}")

        stdscr.addstr(9, 2, "Recent Log:")
        y = 10
        for line in logs:
            stdscr.addstr(y, 4, line[:80])
            y += 1

        stdscr.addstr(20, 2, "[q] Quit   [r] Restore")
        key = stdscr.getch()

        if key == ord('q'):
            break
        if key == ord('r'):
            os.system("python3 restore.py")

        stdscr.refresh()
        time.sleep(1)


if __name__ == "__main__":
    curses.wrapper(curses_ui)
