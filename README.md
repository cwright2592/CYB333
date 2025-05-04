# CYB333 Security Automation Project  
**Christopher Wright**

## Project Title:  
**Socket Programming & Port Scanner**

## Overview  
This project was created as part of CYB333 – Security Automation. It consists of three core Python scripts:
- A socket-based server that listens for connections.
- A client that connects to the server and sends a message.
- A simple port scanner that checks for open ports on a specified host.

The purpose of the project is to demonstrate basic client-server communication using Python’s socket module and explore the concept of port scanning, which is often used in cybersecurity assessments.

---

## Features  
- Simple socket-based client-server messaging
- Localhost and external port scanning (e.g., scanme.nmap.org)
- Clean terminal output for open/closed ports
- Beginner-friendly structure and comments

---

## File List  
- `server.py` – Starts a socket server that listens for incoming messages.
- `client.py` – Connects to the server and sends a simple message.
- `simple_port_scanner.py` – Scans a target IP address and returns open/closed port results.
- `README.md` – This file.

---

## Requirements  
- Python 3.x (tested with 3.10)
- No third-party libraries required

---

## Setup Instructions  

1. **Clone the Repository**  

2. **Run the Server (in Terminal 1)**  

3. **Run the Client (in Terminal 2)**  

4. **Run the Port Scanner**  

When prompted, enter an IP address (e.g., `127.0.0.1` or `scanme.nmap.org`)

---

## Notes  
- Be sure to run the server first before running the client.
- The port scanner will take longer for hosts that drop packets or firewall ports.
- If you're using Windows and see `'python' is not recognized...`, make sure Python is added to your system PATH.

---

## Learning Outcome  
This project taught me how Python sockets work, how to troubleshoot environmental issues (like PATH and file errors), and how to build basic automation tools that interact with network layers. It also introduced me to GitHub and helped build my confidence using the terminal and debugging code.

---

## Author  
**Christopher Wright**  
[GitHub Repository](https://github.com/cwright2592/CYB333)
