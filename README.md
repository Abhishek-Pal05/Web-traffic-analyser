# 🌐 Web Traffic Analyzer using Python

This project captures and analyzes real-time web traffic on your local network. Using Python libraries like **Scapy**, **Pandas**, and **Matplotlib**, it provides insights into network packet flow and visualizes key metrics such as protocol usage and top source IPs.

---

##  Purpose

The primary goal of this project is to help beginners in cybersecurity and networking:
- Understand how packets travel over a network.
- Learn how to capture and parse network data.
- Visualize traffic for better insights and analysis.
- Build foundational skills in Python-based network analysis.

---

##  Features

-  Live packet capture (using Scapy)
-  CSV export of captured packet data
-  Visualizations:
  - Protocol distribution chart
  - Top source IPs bar chart
-  Filter out irrelevant traffic
-  Organized output files (CSV and PNG)

---

##  Terminology

- **Packet**: A formatted unit of data carried by a network.
- **Protocol**: A set of rules used for communication (e.g., TCP, UDP, ICMP).
- **Source IP**: The IP address from which the packet originated.
- **Destination IP**: The IP address to which the packet is being sent.

---

## ⚠ Limitations

- Requires **admin/root privileges** to sniff packets.
- Only works on **local network interface**.
- Not optimized for **high-traffic environments**.
- Designed for **educational purposes** only.

---

##  Requirements

- Python 3.8 or above  
- Install dependencies:
bash
pip install scapy pandas matplotlib

## Further Improvements
1. Add packet filtering by port/protocol
2. Add GUI using Tkinter or PyQt
3. Real-time dashboard using Flask/Plotly
4. Store data in SQLite or MongoDB
5. Detect suspicious or malicious patterns

## Ethical Consideration
This tool is built strictly for learning and ethical use. Unauthorized packet capturing or analysis on networks you do not own or have permission to monitor may violate local laws or privacy regulations. Always use this tool responsibly.
