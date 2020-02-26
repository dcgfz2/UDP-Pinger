#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
import time

client = socket(AF_INET, SOCK_DGRAM)

serverIP = '127.0.0.1'
serverPort = 12000

# Set timeout to 1 sec
client.settimeout(1)


send = ''
avgRTT = 0
packetLoss = 0.0
minRTT = 0.0
maxRTT = 0.0

for num in range(10):
    timeS = time.time() 
    send = 'Ping ' + str(num + 1) + ' '+ str(timeS)
    client.sendto(send.encode(), (serverIP,serverPort))
    
    try:
        recv, orgin = client.recvfrom(1024)
        timeR = time.time()
        RTT = timeR - timeS
        avgRTT += RTT

        if minRTT == 0.0:
            minRTT = RTT
        else:
            if minRTT > RTT:
                minRTT = RTT
        
        if maxRTT < RTT:
            maxRTT = RTT

        print(recv.decode())
        print('RTT: ' + str(RTT) + '\n')
    except timeout:
        print('Request timed out\n')
        packetLoss += 1

print('MIN RRT: ' + str(minRTT))
print('MAX RRT: ' + str(maxRTT))
print('AVG RRT: ' + str(avgRTT/(10-packetLoss)))
print('PACKET LOSS: ' + str((packetLoss/10.0)*100) + '%' )
client.close()
