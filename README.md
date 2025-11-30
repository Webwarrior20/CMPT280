Multi-Victim Worm Simulation + Detection + Recovery (Safe Academic Demo)
Overview

This project demonstrates a safe and reversible multi-victim worm simulation in an isolated environment using Docker, Python, and controlled victim folders. All components are designed for academic and instructional demonstration only. It includes fake credential collection, controlled file modifications, replication, monitoring, and complete restoration.

No real systems or personal data are touched.

Project Architecture
Final_Project/
├─ initial_access/
│   ├─ assignment_helper.py
│   └─ phish_server.py
├─ collected/
│   ├─ simulated_terminal_tokens.txt
│   └─ simulated_web_tokens.txt
├─ malware/
│   ├─ tamper.py
│   └─ Dockerfile
├─ victim1/
├─ victim2/
├─ victim3/
├─ restore.py
├─ monitor.py
├─ detect_intrusion.py
├─ docker-compose.yml
└─ watch_shutdown_and_down.sh

Core Features

• Safe simulation of credential collection
• Token-based victim selection
• Multi-victim propagation
• Controlled file modifications
• Fake payload creation
• Replica spreading
• Logging and event tracing
• Real-time monitoring
• Full restoration after attack
• Automatic shutdown capability

All actions are reversible and limited to the containers and victim folders.

Simulated Initial Access
Terminal Credential Collection
python3 initial_access/assignment_helper.py


Fake credentials are stored in:

collected/simulated_terminal_tokens.txt

Web Credential Collection
python3 initial_access/phish_server.py


Open browser:

http://127.0.0.1:5000


Fake credentials are stored in:

collected/simulated_web_tokens.txt

Start Multi-Victim Containers

Run:

docker-compose up --build


The worm loads all victim folders and waits for a controller command:

[controller] waiting for ATTACK...

Trigger Controlled Infection

In a second terminal:

docker exec -it fp_malware bash
echo ATTACK > /commands/command.txt


Worm will:

• Read simulated credentials
• Select victim folders using hashing
• Perform controlled tampering
• Create fake payloads
• Write logs and manifests

Example activity:

[tamper] assignment1.py
[fake] created cache.bak

Monitoring and Detection
python3 monitor.py


Monitors file changes and prints alerts in real-time.

Full Restoration
python3 restore.py


This restores all modified files, removes fake files and replicas, and resets victim folders.

Restoration is guaranteed safe.

Credential-Based Victim Selection

Simulated credentials determine which victims are selected using hashing:

hash(username) % number_of_victims


Example mapping:

bob  → victim2
alice → victim1


This simulates credential-based lateral movement safely.

Shutdown Support

To automatically shut down the environment:

./watch_shutdown_and_down.sh


When the worm finishes, containers are brought down safely.

Security and Ethics

This project:

• Uses only fake and simulated credentials
• Does not act on real networks
• Propagation exists only within Docker folders
• All actions are reversible
• Designed for education and controlled cybersecurity demonstration

This is not real malware.

Requirements

• Python 3.10+
• Docker and docker-compose
• Flask (if running the web portal)

Install Flask:

pip3 install flask

Troubleshooting

If restore script requires permissions:

sudo python3 restore.py


If containers fail to start:

docker-compose down
docker-compose up --build

Educational Value

This project demonstrates:

Concept	Included
Multi-stage infection chain	✔
Credential-based targeting	✔
Replication and propagation	✔
File tampering	✔
Manifest logging	✔
Detection and monitoring	✔
Full restore	✔
Automatic shutdown	✔
