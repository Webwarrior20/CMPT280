#!/usr/bin/env bash

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# check all victim directories dynamically
VICTIMS=("$PROJECT_ROOT"/victim*)

echo "[watcher] Watching shutdown flags in:"
for v in "${VICTIMS[@]}"; do
  echo "  => $v/.shutdown"
done

while true; do
  for v in "${VICTIMS[@]}"; do
    if [ -f "$v/.shutdown" ]; then
      echo "[watcher] Shutdown flag found in $v"
      echo "[watcher] Running docker-compose down..."
      docker-compose down
      exit 0
    fi
  done

  sleep 2
done
