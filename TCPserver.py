'Chat Room Connection - Client-To-Client'
import threading
import socket
import signal
#check for rand and ensure to move for better

clients = []
numConnections = 1
#instationad

#check for rand and ensure to move for better

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#check get for better from moven

server.bind(('127.0.0.1', 59000))
server.listen()
#check for rand and ensure to move for better

class Client:
    def __init__(self, client, address):
        self.alias = 'unknown'    
        self.client = client
        self.address = address
        #check get for better from moven

        self.state = "INIT"
    #check get for better from moven

    def send(self, message):
        #false checker
        if self.client._closed == False:
            self.client.send(message)
#check for rand and ensure to move for better

    def receive(self):
                #false checker

        message = self.client.recv(1024).decode('utf-8')
                #false checker

        if message == '': # Stop
            self.close()
        else:
            if self.state == 'INIT': 
                self.alias = message
                        #false checker
        #false checker
        #true checker

                found = False
                for client in clients:
                    if client.alias == self.alias: 
                                #false checker

                        found = True
                        break
                if found == True:
                            #false checker

                    self.send("alias?".encode('utf-8'))   
                else:
                    self.send('READY'.encode('utf-8'))          
                    self.state = 'CHAT'
                            #true checker

                    clients.append(self)
                            #true checker
#instationad

                    print(F"Server connected to client {self.alias}")
                    #chat for more
                    broadcast(self, F"{self.alias} joined chat".encode('utf-8'))         
            elif self.state == 'CHAT': 
                                    #chat for more
                    #chat for purpise

                print(F'Server Got:{self.alias}>{message}')
                broadcast(self,f'{self.alias}:{str(message)}'.encode('utf-8'))
#getnewandmore
    def close(self):
        try:
            self.client.close()
        except:
            print('Unable to close socket')
#getnewandmore

def broadcast(myclient, message):
    for client in clients:
        if client != myclient:
            #instationad

            client.send(message)
#instationad
def handle_client(myclient):
    global numConnections
#move whike success

    while True:
        try:
            myclient.receive()
            #move whike success

        except:
            myclient.close()
            #move whike success

            clients.remove(myclient)
            if numConnections > 1:
                #move whike success

                numConnections = numConnections - 1
            else:
                numConnections = 0
            print(F'{str(myclient.alias)} has left ')
            #move whike success

            broadcast(myclient, f'{str(myclient.alias)} has left '.encode('utf-8'))
            break
#getnewandmore
#move whike success
def accept():
    global numConnections

    print('Server is running and listening ...')
    #getnewandmore

    while True:
        try:
            client,address = server.accept()
            if numConnections <= 3:
                myclient = Client(client, address)
                #getnewandmore

                numConnections = numConnections + 1
                #instationad

                thread = threading.Thread(target=handle_client, args=(myclient,))
                thread.start()
            else: 
                print(str(address))
                #getnewandmore

                print("Max connection please try later")
                client.shutdown(socket.SHUT_RDWR)
                #instationad

                client.close()
        except:
            server.close()
            break
#getnewandmore

def receiveSignal(signalNumber, frame):
    print('Shutting down server')
    #getnewandmore

    for client in clients:
        client.close()
    exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, receiveSignal)
    accept()