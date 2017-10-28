import thread as th
import os
import socket, random
from time import sleep

INTERVAL_TIME = 2
RAMESH_PRINT_HEADER = "\033[0;1;32mRAMESH: \033[0;39m"
SURESH_PRINT_HEADER = "\033[0;1;33mSURESH: \033[0;39m"

def ramesh():
    s = socket.socket()
    host = socket.gethostname()
    s.connect((host, 7777))
    s.send(RAMESH_PRINT_HEADER+"Hi Suresh.. Remember me, Ramesh? We used to star in the 5 star ad.")
    print s.recv(1024)
    sleep(INTERVAL_TIME)
    s.send(RAMESH_PRINT_HEADER+"Acha okay! Send me one :D")
    encr = s.recv(1024)
    os.system("openssl pkeyutl -decrypt -in signed_num.bin -inkey privkey-Ramesh.pem -out received.txt")
    decr=0
    with open("received.txt") as f:
        decr = int(f.read())
    decr-=1
    s.send(RAMESH_PRINT_HEADER+"I received your challenge. I am sending you the response but it includes my challenge as well. Format is response, challenge")
    print s.recv(1024)
    sleep(INTERVAL_TIME)
    n = random.randint(1,100)
    what_to_encrypt = str(decr)+","+str(n)
    os.system("echo "+what_to_encrypt+" > what.txt")
    os.system("openssl pkeyutl -encrypt -in what.txt -pubin -inkey pubkey-Suresh.pem -out signed_num.bin")
    with open('signed_num.bin') as f:
        s.send(str(f.read()))
    print s.recv(1024)
    sleep(INTERVAL_TIME)
    s.send(RAMESH_PRINT_HEADER+"Good. Ok")
    r=int(s.recv(1024))
    if r==n-1:
        s.send(RAMESH_PRINT_HEADER+"Hi Suresh. Hope we trust each other now. So, I wanted to ask you.... How about one more 5 star ad?")
        print s.recv(1024)
    s.close()


def suresh():
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, 7777))
    s.listen(1)
    r,_ = s.accept()
    print r.recv(1024)
    sleep(INTERVAL_TIME)
    r.send(SURESH_PRINT_HEADER+"Hey! I don't trust you. Prove me you are Ramesh. I will give you a number return me that number-1.")
    print r.recv(1024)
    sleep(INTERVAL_TIME)
    n = random.randint(1,100)
    os.system("echo "+str(n)+" > what.txt")
    os.system("openssl pkeyutl -encrypt -in what.txt -pubin -inkey pubkey-Ramesh.pem -out signed_num.bin")
    with open('signed_num.bin') as f:
        r.send(str(f.read()))
    print r.recv(1024)
    sleep(INTERVAL_TIME)
    r.send(SURESH_PRINT_HEADER+"Ok")
    encr = r.recv(1024)
    sleep(1)
    os.system("openssl pkeyutl -decrypt -in signed_num.bin -inkey privkey-Suresh.pem -out received.txt")
    sleep(1)
    decr=""
    with open('received.txt') as f:
        decr = f.read().split(",")
    if (n-1)==int(decr[0]):
        r.send(SURESH_PRINT_HEADER+"Hi Ramesh! I am sorry I doubted you. I am sending you my response now")
        print r.recv(1024)
        sleep(INTERVAL_TIME)
        n=int(decr[1])-1
        r.send(str(n))
        print r.recv(1024)
        sleep(INTERVAL_TIME)
        r.send(SURESH_PRINT_HEADER+"Nooo................!!!!! :/ ")
        sleep(INTERVAL_TIME)
        print('\nThe End. Press any key to exit.')
        r.close()
        s.close()

if __name__ == "__main__":
    ''' print "Creating private & public key pairs...."
    os.system("openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:3 -out privkey-Ramesh.pem")
    os.system("openssl pkey -in privkey-Ramesh.pem -out pubkey-Ramesh.pem -pubout")
    os.system("openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:3 -out privkey-Suresh.pem")
    os.system("openssl pkey -in privkey-Suresh.pem -out pubkey-Suresh.pem -pubout") '''
    print "\nHere is a conversation between two friends:\n"
    th.start_new_thread(ramesh, ())
    th.start_new_thread(suresh, ())
    raw_input()