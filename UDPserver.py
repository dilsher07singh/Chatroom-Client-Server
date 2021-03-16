import socket
import sys

import select
from _thread import *

#changefor
#get comments
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#variables
randvar=0
maxusersR = 4

server.bind(('127.0.0.1', 50000))
#variables

randvar2=1
#variables

clientfoundL = []


print ("Chatroom Created UDP Side Elec3120")

 
while 1 :
        newmess, adress = server.recvfrom(2048)
#variables

        randvar3=1


        if adress in clientfoundL:

#variables

            newmess.decode()

            changethismess = newmess.decode()
#variables here

            print(str(changethismess))
            turntotrue=1

            for varcli in clientfoundL:

#variables declaration

                if varcli != adress :
                    server.sendto(newmess, varcli)
                    
        else :
            if (maxusersR>len(clientfoundL)):
                clientfoundL.append(adress)
#changefor

                messagerand = newmess.decode()
#changefor

                randstateStart = str(newmess) + " has entered the chatroom!"
#changefor

                print(randstateStart)

                firstcheck = "ELEC3120 Chatroom"

                server.sendto(firstcheck.encode(),adress)
                for varcli in clientfoundL:
#check varcli
                    if varcli != adress:

                        server.sendto(randstateStart.encode(), varcli)

            else : 
                randvar5=1

                worstcase = "Sorry room is full"

                checkertrue=0

                print("<"  + adress[0] + " , " + str(adress[1]) +  "> " + "was blocked based on condition")

                server.sendto(worstcase.encode(),adress)

