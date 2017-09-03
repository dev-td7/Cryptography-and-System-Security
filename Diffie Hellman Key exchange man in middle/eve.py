import socket
import public
import random as r
from struct import *

"""
first:          Who starts sending first.
second:         To whom does first send.
z:              Private value with Eve.
val_to_be_sent: The manipulated value that Eve sends.
"""
first = "Alice"
second = "Bob"
z = r.randint(2, public.MAX_VAL)
val_to_be_sent = (public.g ** z) % public.p

s = socket.socket()
host = socket.gethostname()
s.bind((host, public.port_eve))
print "Eve is up & running\n"
print "Manipulated value by Eve: "+str(val_to_be_sent)+"\n"
s.listen(1)
client, _ = s.accept()
who_starts_first = int(client.recv(1024))
client.send("ok")
if who_starts_first is 1:
    first = "Bob"
    second = "Alice"
val = int(client.recv(1024))
print "Received "+str(val)+" from "+first
s.close()

s = socket.socket()
port = public.get_port_no(who_starts_first)
connected_to = public.get_name(port)
print "Eve connecting to "+second
s.connect((host, port))
s.send(str(val_to_be_sent))
print "Sent "+str(val_to_be_sent)+" to "+second
val = int(s.recv(1024))
print "Received "+str(val)+" from "+second
s.close()

print "Sending "+str(val_to_be_sent)+" to "+first
client.send(str(val_to_be_sent))
client.close()
