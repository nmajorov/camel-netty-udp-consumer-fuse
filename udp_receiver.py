# simple udp receiver written in python v.3
# Nikolaj Majorov nikolaj@majorov.biz


import socket
import struct
import sys
    
UDP_GROUP = "239.193.192.3"
UDP_PORT=25001
server_address = ('',UDP_PORT)
   
sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

#tell os to add the socket to the multicast group
sock.bind(server_address)
group=socket.inet_aton(UDP_GROUP)
mreq=struct.pack('4sL',group,socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)



print ("start server on multicast group: {0} port: {1}".format(UDP_GROUP,UDP_PORT))     
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:", data)
