from scapy.all import *
#
#
# def packet_callback(packet):
#     # if packet[TCP_SERVICES].payload:
#     #     mail_packet = str(packet[TCP_SERVICES].payload)
#     #     if 'user' in mail_packet.lower() or 'pass' in mail_packet.lower():
#     #         print('[*] Server: {}'.format(packet[IPField]))
#     #         print('[*] {}'.format(packet[TCP_SERVICES].payload))
#     print(packet.show2())
#
#
# sniff(prn=packet_callback, count=1, store=0)

# Change your theme: DefaultTheme, BrightTheme, RastaTheme, ColorOnBlackTheme, BlackAndWhite, HTMLTheme, LatexTheme
conf.color_theme = BrightTheme()

# build a packet and play with it

a = IP(ttl=10)
print(a)
print(a.src)
