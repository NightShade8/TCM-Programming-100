# 🔍 Port Scanner - Capstone Project

Welcome to the **Port Scanner** project! This script is a multithreaded Python program designed to scan all 65,535 ports on a target machine to identify open ports. It is part of the **TCM Programming 100** course capstone project.

---

## 📄 Description

The `Scanner.py` script allows users to scan a target machine's ports to identify which ones are open. It uses Python's `socket` module for network communication and `threading` to perform concurrent scans, making it efficient for large-scale port scanning.

---

## 🚀 Features

- **Port Scanning**: Scans all ports (1–65,535) on a target machine.
- **Multithreading**: Uses threads to scan ports concurrently, improving performance.
- **Error Handling**: Handles socket errors and unexpected exceptions gracefully.
- **Hostname Resolution**: Resolves the target hostname to an IP address.
- **User-Friendly Output**: Displays open ports and a summary of the scan.

---

## 🛠️ How It Works

1. **Input**: The script takes a single argument, the target hostname or IP address.
2. **Hostname Resolution**: Converts the hostname to an IP address using `socket.gethostbyname()`.
3. **Port Scanning**: Iterates through all ports (1–65,535) and checks if they are open using `socket.connect_ex()`.
4. **Multithreading**: Each port scan runs in a separate thread for faster execution.
5. **Output**: Displays open ports and a summary of the scan, including the start time.

---

## 📋 Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Script
1. Open a terminal.
2. Run the script with the following command:
   ```bash
   python Scanner.py <target>