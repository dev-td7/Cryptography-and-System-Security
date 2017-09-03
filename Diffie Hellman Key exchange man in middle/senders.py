import public as p
import socket
import thread as th
import random as r

private_alice = r.randint(2, p.MAX_VAL)
private_bob = r.randint(2, p.MAX_VAL)

def server(who, port, private_no):
    print who+" is up & running as server\n"
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(1)
    client, _ = s.accept()
    k1 = int(client.recv(1024))
    print(who+" received "+str(k1))
    k = (k1**private_no) % p.p
    print "The secret key with "+who+" is: "+str(k)
    val = (p.g**private_no)%p.p
    print who+" sent "+str(val)
    client.send(str(val))
    client.close()

def client(who, port, private_no):
    print who+" is up & running as client.\n"
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host, port))
    val = (p.g**private_no) % p.p
    print(who+" sent "+str(val))
    s.send(str(who_starts_first))
    s.recv(1024)
    s.send(str(val))
    k1 = int(s.recv(1024))
    print(who+" received "+str(k1))
    k = k1**private_no % p.p
    print("The secret key with "+who+" is: "+str(k))
    s.close()

who_starts_first = r.randint(0,1)
"""
who_starts_first:
    0 -> Alice starts sending to Bob.
    1 -> Bob starts sending to ALice.
"""
if who_starts_first == 0:
    th.start_new_thread(client, ("Alice", p.port_eve, private_alice,) )
    th.start_new_thread(server, ("Bob", p.port_bob, private_bob,) )
else:
    th.start_new_thread(client, ("Bob", p.port_eve, private_bob,) )
    th.start_new_thread(server, ("Alice", p.port_alice, private_alice,) )

########## Very Very Important for threads to abstain from termination! ############
_ = raw_input()