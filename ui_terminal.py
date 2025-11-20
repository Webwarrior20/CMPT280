#!/usr/bin/env python3
import curses
import os
import time
from datetime import datetime
from pathlib import Path
import shutil

TARGET_DIR = Path(os.environ.get("TARGET_DIR", "./victim/assignments")).resolve()
TRASH_DIR = TARGET_DIR / ".trash_demo_backup"
LOGFILE = TARGET_DIR / ".simworm_log.txt"

FAKE_NAMES = {
    "results.tmp",
    "cache.bak",
    "system32.dll.fake",
    "report_copy.docx.fake",
    "submission_v2.py.bak",
}

def get_stats():
    total_files = 0
    fake_files = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        if TRASH_DIR in Path(root).parents or Path(root) == TRASH_DIR:
            continue
        for f in files:
            total_files += 1
            if f in FAKE_NAMES:
                fake_files += 1
    backups = 0
    if TRASH_DIR.exists():
        backups = sum(1 for _ in TRASH_DIR.iterdir() if _.is_file())
    return total_files, backups, fake_files

def tail_log(n=15):
    if not LOGFILE.exists():
        return ["(no log file yet)"]
    try:
        with open(LOGFILE, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except Exception as e:
        return [f"(error reading log: {e})"]
    return lines[-n:] if len(lines) > n else lines

def restore_from_backups():
    if not TRASH_DIR.exists():
        return "No backups directory found."
    restored = 0
    for backup_file in sorted(TRASH_DIR.iterdir(), key=lambda p: p.stat().st_mtime):
        if not backup_file.is_file():
            continue
        name_part = backup_file.name.split("_", 1)[-1]
        if name_part.endswith(".orig"):
            name_part = name_part[:-5]
        restore_path = TARGET_DIR / name_part
        try:
            restore_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(backup_file, restore_path)
            restored += 1
        except Exception:
            pass
    return f"Restore completed. Files restored: {restored}"

def ui_loop(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    height, width = stdscr.getmaxyx()
    last_message = ""

    while True:
        stdscr.erase()
        now = datetime.now().strftime("%H:%M:%S")
        stdscr.addstr(0, 0, f"Simulated Worm Monitor | TARGET_DIR={str(TARGET_DIR)}")
        stdscr.addstr(1, 0, f"Time: {now}")
        stdscr.addstr(2, 0, "Keys: [r] restore  [q] quit")

        total_files, backups, fake_files = get_stats()
        stdscr.addstr(4, 0, f"Total files       : {total_files}")
        stdscr.addstr(5, 0, f"Backup files      : {backups}")
        stdscr.addstr(6, 0, f"Fake files (decoy): {fake_files}")

        if last_message:
            stdscr.addstr(8, 0, f"Last action: {last_message[:width-1]}")

        stdscr.addstr(10, 0, "Log tail (.simworm_log.txt):")
        log_lines = tail_log()
        row = 11
        for line in log_lines:
            if row >= height - 1:
                break
            txt = line.rstrip()
            stdscr.addstr(row, 0, txt[:width-1])
            row += 1

        stdscr.refresh()

        try:
            ch = stdscr.getch()
        except curses.error:
            ch = -1

        if ch == ord("q"):
            break
        elif ch == ord("r"):
            last_message = restore_from_backups()

        time.sleep(0.5)

def main():
    if not TARGET_DIR.exists():
        print(f"ERROR: TARGET_DIR {TARGET_DIR} does not exist.")
        return
    curses.wrapper(ui_loop)

if __name__ == "__main__":
    main()
