import socket
from struct import *

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
blacklist=['151.101.64.133', '111.221.29.254','151.101.36.133','114.143.198.3']
all_ips_handled, all_ips_blocked = set(), set()
while True:
    try:
        r = s.recvfrom(65535)[0]
        ip_header_array = r[0:20]
        ip_header_array = unpack('!BBHHHBBH4s4s' , ip_header_array)
        incoming_ip = socket.inet_ntoa(ip_header_array[8])
        if str(incoming_ip) in blacklist:
            all_ips_blocked.add(incoming_ip)
            print 'Request from', incoming_ip, 'blocked'
        else:
            print 'Incoming request from '+incoming_ip
            all_ips_handled.add(incoming_ip)
    except KeyboardInterrupt:
        print 'Stopped spoofing IPs\n\nAll IPs handled:'
        for ip in all_ips_handled: print ip
        print '\nThe IPs that were blocked:'
        for ip in all_ips_blocked: print ip
        break
    except Exception:
        print 'This IP spoofer only runs on Ubuntu :(. Will make one for windows soon!'

"""
---------------
Sample output:
---------------

Request from 151.101.36.133 blocked
Request from 151.101.36.133 blocked
Request from 151.101.36.133 blocked
^CStopped spoofing IPs

All IPs handled:
192.30.253.125
151.101.1.69

The IPs that were blocked:
151.101.36.133
111.221.29.254

"""