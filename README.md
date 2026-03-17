# Social-Engineering-Spyware-Demo
⚠️ DISCLAIMER: This project is strictly for academic and educational purposes only. It was developed as part of the Information Security course at FAST-NUCES. Deploying this application against real users is illegal and unethical.


📋 Overview
A proof-of-concept social engineering web application that demonstrates how malicious actors exploit user trust to harvest sensitive data. Disguised as a harmless "Jawline Score Checker", this app tricks users into granting camera and location permissions, then secretly records and exfiltrates their data to Google Drive.
Course: Information Security — Assignment 3
Institution: FAST-NUCES
Academic Year: 2024–25, Spring Semester

👥 Group Members
NameRoll NumberMuhammad Mursaleen Mustafvi23F-0659Muhammad23F-0577

🧠 What This Demonstrates

Social Engineering — Using a vanity-based pretext to lure users
Browser API Abuse — Misuse of getUserMedia() and Geolocation APIs
Silent Data Exfiltration — Covert upload to attacker-controlled cloud storage
False Reward Mechanism — Fake scores to prevent immediate suspicion
OAuth Token Abuse — Pre-authenticated Google Drive access


🗂️ Project Structure
IS-Assignment-3/
├── index.html          # Frontend UI — Jawline Score Checker
├── script.js           # JS logic: recording, GPS, upload, fake score
├── style.css           # Styling
├── server.py           # Flask backend — receives data, uploads to Drive
├── client_secret.json  # Google OAuth2 credentials (not included)
├── token.pickle        # Cached OAuth token (not included)
└── package.json        # Node.js config

⚙️ Tech Stack

Frontend: HTML5, CSS3, JavaScript (MediaRecorder API, Geolocation API)
Backend: Python, Flask
Cloud: Google Drive API v3
Auth: OAuth 2.0


🔄 Attack Flow
User visits site
     ↓
Lured by "Jawline Score" pretext
     ↓
Grants camera + microphone + location
     ↓
JS records 10s video/audio silently
     ↓
GPS coordinates collected
     ↓
POST /upload → Flask server
     ↓
Uploaded to attacker's Google Drive
     ↓
Fake score displayed (85–100/100)

🛡️ Defences & Mitigations
DefenceWho It TargetsBe skeptical of unsolicited permission requestsUserAudit browser permissions regularlyUserContent Security Policy (CSP) headersDeveloperHTTPS enforcementDeveloperRate limit upload endpointsDeveloperStore OAuth tokens encryptedDeveloperSecurity awareness trainingOrganization

📚 Key Learning Outcomes

Understanding how social engineering attacks are constructed
Browser API misuse vectors and how to defend against them
Silent data exfiltration techniques
Importance of user education in security posture


⚖️ Ethical Statement
This project was developed in a controlled academic environment. No real users were targeted. All tests were performed on self-owned devices. The goal is education — understanding attacks is the first step to defending against them.

FAST-NUCES | Department of Computer Science | Information Security
