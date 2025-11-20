# CMPT280 Final Project – Assignment Tampering + Simulated Worm Attack

## 📌 Overview
This project is a **safe, academic simulation of malware behavior**. It demonstrates:

- File tampering via comment injection
- Recursive “worm-like” replication
- Creation of decoy files
- Backup + restore functionality
- Monitoring via a terminal-based UI

All operations occur only inside the mapped `/assignments` directory and **are reversible**.

⚠ **Educational use only — do not run outside a controlled VM.**

---

## 📂 Project Structure


---

## 🐳 Running the Project

### **1️⃣ Build & run containers**

From project root:

```bash
docker-compose up --build

docker exec -it fp_victim bash
ls

TARGET_DIR=./victim/assignments python3 ui_terminal.py

