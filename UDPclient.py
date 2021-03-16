import select

import socket
import sys
#more for the same checker

duplicateval = input("Please Enter The username: ")

morevarto=5
#get comment to move around

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
morevartoq=5

#get comment to move around
adressuse = ('127.0.0.1', 50000)
#more for the same checker
while 1:

	morevartoh=5
#more for the same checker

	sockets_list = [sys.stdin, server]
	read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
#more for the same checker


	for changetoS in read_sockets:
#more for the same checker

		if changetoS == server:
			getformess, serv = changetoS.recvfrom(2048)
			morevartoj=5

			print (getformess.decode())
			if getformess.decode() == "Sorry room is full":
				exit()

			
#more for the same checker

		else:
			getformess = sys.stdin.readline()
			#more for the same getform syst

			getformessN = "<" + str(duplicateval) + "> " + getformess
			#get comment to move around

			#more for the same string

			morevartog=5
#more for the same checker
			newchecker=1
			newcheckerD=0
			#get var to change as per req

			server.sendto(str.encode(getformessN),adressuse)
			sys.stdout.flush()

