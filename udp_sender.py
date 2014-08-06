#!/usr/bin/env python

# udp sender written in python3 syntax -> read message from input and send it
#
# Nikolaj Majorov nikolaj@majorov.biz

import socket

UDP_GROUP = "239.193.192.3"
UDP_PORT =  25001

  
print ("multicast group:", UDP_GROUP)
print ("UDP target port:", UDP_PORT)
try:   
        sock = socket.socket(socket.AF_INET, # Internet
                                socket.SOCK_DGRAM) # UDP

        # Make the socket multicast-aware, and set TTL.
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 20) # Change TTL (=20) to suit
except socket.error as e:
       print ('Error Code : ' + str(e[0]) + ' Message ' + e[1])
       sys.exit()

 # Ctrl + C
except KeyboardInterrupt:
       sys.exit()

if  __name__ =='__main__':
    while True:
        msg = input("send udp  message -->")
        print ("sending message {0}".format(msg))
        sock.sendto(msg.encode('utf-8'), (UDP_GROUP, UDP_PORT))
