from scapy.all import sniff, Dot11

def show_wifi(pkt):
    if pkt.haslayer(Dot11):
        print(pkt.summary())

sniff(iface="wlan0", prn=show_wifi , store=False)
