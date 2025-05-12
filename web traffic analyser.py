import pandas as pd
import matplotlib.pyplot as plt
from scapy.all import sniff, IP, TCP, UDP
import os

# List to store packet data
packet_data = []

# Function to process packets and extract required data
def process_packet(packet):
    if IP in packet:  # Only process IP packets
        packet_info = {
            'Timestamp': packet.time,
            'Source IP': packet[IP].src,
            'Destination IP': packet[IP].dst,
            'Protocol': packet.proto,
            'Length': len(packet)
        }
        packet_data.append(packet_info)  # Append packet data to the list

# Function to start sniffing
def start_sniffing(packet_count):
    print(f"[*] Starting packet capture for {packet_count} packets...")
    sniff(prn=process_packet, filter="ip", store=False, count=packet_count)
    print("[*] Packet capture complete.")

# Function to analyze and visualize the captured packets
def analyze_and_visualize():
    start_sniffing(packet_count=100)  # Capture 100 packets
    
    # Convert packet data into a DataFrame
    df = pd.DataFrame(packet_data)
    
    # Save captured packets data to a CSV file on Desktop
    output_path = output_path = "/Users/abhishekpal/Documents/captured_packets.csv"

    df.to_csv(output_path, index=False)
    print(f"[*] Captured packet data saved to {output_path}")
    
    # Example: Visualizing Protocol Distribution
    protocol_counts = df['Protocol'].value_counts()
    protocol_counts.plot(kind='bar', title="Protocol Distribution")
    plt.savefig("/Users/abhishekpal/Documents/protocol_distribution.png")


    
    # Example: Visualizing Top Source IPs
    top_source_ips = df['Source IP'].value_counts().head(10)
    top_source_ips.plot(kind='bar', title="Top 10 Source IPs")
    plt.savefig("/Users/abhishekpal/Documents/top_source_ips.png")


# Run the analysis and visualization
analyze_and_visualize()
