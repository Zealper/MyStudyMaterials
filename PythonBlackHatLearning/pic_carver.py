from scapy.all import *

pcaps = rdpcap('/Users/zealper/Desktop/MyStudyMaterials/PythonBlackHatLearning/arper.pcap')
print(pcaps[0].show())