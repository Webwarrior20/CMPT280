Final Project (Assignment Tampering Demo)
----------------------------------------

This archive contains a safe, demo-ready project for an "assignment tampering" proof-of-concept
to be run in an isolated environment (Docker/VM). Files included:

- docker-compose.yml
- victim/Dockerfile
- victim/assignments/assignment1.py
- victim/assignments/assignment2.py
- malware/Dockerfile
- malware/tamper.py (SAFE demo variant; moves "deleted" files to .trash_demo)

IMPORTANT SAFETY NOTE:
- Do NOT run this on a production host or with bind-mounts pointing at important data.
- The malware container operates on the mounted assignments folder. For local testing the compose uses a host bind-mount
  of ./victim/assignments. If you want to avoid modifying host files, edit docker-compose.yml to use a Docker volume instead.

Quick start (from project root):
    docker-compose up --build

Inspect victim container:
    docker exec -it fp_victim bash
    ls -la /home/victim/assignments
    python3 /home/victim/assignments/assignment1.py 7

