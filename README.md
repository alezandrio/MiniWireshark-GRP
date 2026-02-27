# MiniWireshark-GRP

MiniWireshark is a simple, educational network packet sniffer inspired by Wireshark. It captures raw network traffic directly from the network interface and decodes key protocol fields, allowing you to explore how packets are structured and how data flows across a network. Designed for learning, debugging, and experimentation, it provides a minimal yet functional look into packet¿level networking without the complexity of full¿scale analysis tools.

# Features

- Real¿time packet capture from a chosen network interface
- Parsing of common protocols (Ethernet, IPv4/IPv6, TCP, UDP, ICMP, etc.)
- Human¿readable packet breakdowns
- Lightweight codebase ideal for study and extension
- Cross¿platform support depending on OS capture capabilities

# Tech Stack 

- Python + Scapy (library)

# Quick Start

## Prerequisites

- Python 3.11.9
- Scapy 2.7.0

## Instalation

1. Clone the repository

```bash
git clone git@github.com:alezandrio/MiniWireshark-GRP.git
```

2. Install dependencies

```bash
cd MiniWireshark-GRP; pip install -r requirements.txt
```

3. Run program

```bash
python main.py
```
