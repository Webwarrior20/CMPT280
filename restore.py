#!/usr/bin/env python3
"""
Restore utility (safe & permission-aware)

- Restores all backup files from assignments/.trash_demo_backup
- Removes fake files
- Tries to log restore events to per-victim manifest.log
- If manifest is not writable, logs to ./restore_manifest.log instead
"""

from pathlib import Path
from datetime import datetime
import shutil, hashlib, os

# All victim directories: victim1, victim2, ...
VICTIMS = [
    p for p in Path(".").resolve().glob("victim*")
    if p.is_dir()
]

FAKE_FILE_NAMES = [
    "results.tmp",
    "cache.bak",
    "system32.dll.fake",
    "report_copy.docx.fake",
    "submission_v2.py.bak",
]


# ------------------------------------------------------
# Hash util (for potential verification / extension)
# ------------------------------------------------------

def file_hash(path: Path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except Exception:
        return None


# ------------------------------------------------------
# Manifest logging (with safe fallback)
# ------------------------------------------------------

def record_restore(assign_dir: Path, path: Path):
    """
    Try to log to victim assignments/manifest.log.
    If that fails (permissions), log to project-level restore_manifest.log instead.
    """
    manifest = assign_dir / "manifest.log"
    entry = f"{datetime.now().isoformat()} | restore | {path.name}\n"

    # First, try per-victim manifest
    try:
        with open(manifest, "a", encoding="utf-8", errors="ignore") as f:
            f.write(entry)
        return
    except PermissionError:
        # Can't write to this manifest -> fall back to global log
        pass
    except Exception:
        # Any other error: also fall back instead of crashing
        pass

    # Fallback manifest in project root
    fallback = Path("restore_manifest.log")
    try:
        with open(fallback, "a", encoding="utf-8", errors="ignore") as g:
            g.write(f"[NOACCESS {manifest}] {entry}")
    except Exception as e:
        # Absolute last resort: just print, but do not crash restore
        print(f"[restore] could not log restore for {path} ({e})")


# ------------------------------------------------------
# Restore a single victim
# ------------------------------------------------------

def restore_victim(victim_dir: Path):
    """
    For each victim:
    - Look in victim/assignments/.trash_demo_backup
    - Restore each backup into victim/assignments
    - Remove fake files in victim/assignments
    """
    assign_dir = victim_dir / "assignments"

    trash = assign_dir / ".trash_demo_backup"
    if not trash.exists():
        print(f"[restore] no trash in {assign_dir}")
        return

    print(f"[restore] restoring victim {victim_dir}")

    # Restore files from backup
    for backup in sorted(trash.iterdir(), key=lambda p: p.stat().st_mtime):
        if not backup.is_file():
            continue

        original_name = backup.name.split("_", 1)[-1]

        if original_name.endswith(".orig"):
            original_name = original_name[:-5]

        dst = assign_dir / original_name  # restore into assignments/
        try:
            shutil.copy2(backup, dst)
            record_restore(assign_dir, dst)
        except PermissionError as e:
            print(f"[restore] cannot restore {dst}: {e}")
            continue
        except Exception as e:
            print(f"[restore] error restoring {dst}: {e}")
            continue

    # Remove fake files from assignments/
    for name in FAKE_FILE_NAMES:
        fp = assign_dir / name
        if fp.exists():
            try:
                fp.unlink()
                record_restore(assign_dir, fp)
            except PermissionError as e:
                print(f"[restore] cannot remove fake file {fp}: {e}")
            except Exception as e:
                print(f"[restore] error removing fake file {fp}: {e}")

    # Optional verification (non-fatal)
    print(f"[verify] {assign_dir}")
    for restored in assign_dir.iterdir():
        if restored.is_file():
            file_hash(restored)


# ------------------------------------------------------
# Main
# ------------------------------------------------------

def main():
    print("[restore] Starting restore...")

    for v in VICTIMS:
        restore_victim(v)

    print("[restore] Done.")


if __name__ == "__main__":
    main()
