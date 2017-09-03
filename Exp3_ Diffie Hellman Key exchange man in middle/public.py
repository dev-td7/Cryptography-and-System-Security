p = 11
g = 7
port_alice = 7777
port_eve = 7780
port_bob = 7779
s = 1
MAX_VAL=25

ports = {1: port_alice, 0: port_bob}
names = {port_alice: 'Alice', port_bob: 'Bob'}
def get_port_no(whose):
    return ports[whose]

def get_name(which_port):
    return names[which_port]
