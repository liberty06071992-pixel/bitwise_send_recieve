from scapy.all import IP, UDP, Raw, send
import time

def simulate_board_signal(target_ip, command_bits):
    # Craft a custom packet with your bitwise data as the payload
    # command_bits is a 16-bit integer (e.g., 0b00001101)
    payload = command_bits.to_bytes(2, byteorder='big')
    
    packet = IP(dst=target_ip) / UDP(dport=12345) / Raw(load=payload)
    send(packet, verbose=False)

# Simulate a sequence of signals
signals = [0x01, 0x02, 0x04, 0x08] # Walking bit pattern
for s in signals:
    print(f"Sending signal: {bin(s)}")
    simulate_board_signal("192.168.1.10", s)
    time.sleep(0.5)
