# ProcessMonitoringProject

##  Overview
This project is a simple **Process Monitoring System** with:
- **Agent (Python)** → collects running process info (PID, name, CPU, memory, hostname) using `psutil` and sends it to the backend.
- **Backend (Django + DRF)** → REST API that receives and stores process data in SQLite.
- **Frontend (HTML + JS)** → Fetches and displays latest processes in a clean UI.

---
Build Instructions

1. Django Backend
-----------------
a) Clone the repo:
   git clone https://github.com/amruth1010/ProcessMonitoringProject.git
b) Navigate to backend:
   cd ProcessMonitoringProject/backend
c) Install dependencies:
   pip install -r requirements.txt
d) Run the server:
   python manage.py runserver
   Access at http://127.0.0.1:8000/

2. Agent (Python)
-----------------
a) Navigate to agent folder:
   cd ProcessMonitoringProject/agent
b) Run directly:
   python agent.py
c) To compile to EXE:
   pip install pyinstaller
   pyinstaller --onefile agent.py
   EXE will be in the 'dist' folder.

3. Frontend
-----------
a) Open frontend/index.html in a browser

4. Any Configuration
-------------------
- Default Django port: 8000
- Agent runs on Windows

