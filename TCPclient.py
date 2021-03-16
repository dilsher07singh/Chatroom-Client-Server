import threading
import socket
import signal
#check for rand and ensure to move for better
state = 'INIT'
#check for rand and ensure to move for better

alias = input('Please enter a username ') 
#check for rand and ensure to move for better

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(('127.0.0.1', 59000))  
client.send(alias.encode('utf-8'))

def client_receive():
    #check for rand and ensure to move for better

    global state
    while True:
        try:
            message = client.recv(1024).decode('utf-8') #recieving from other clients
            if message == "alias?": 
                #variable instantiation

               alias = input('Server Response: Duplicate alias found. Choose unique alias >>> ') #enter alias 
               #variable instantiation

               client.send(alias.encode('utf-8')) #send our alias
            elif state == "INIT":
                state = 'CHAT'
                send_thread = threading.Thread(target=client_send)
                #variable checker

                send_thread.start()
                                #variable checker
                #variable final

            elif message == '':
                state = 'STOP'
                break
                #variable instantiation
#printer
            else:
                print(message)
        except:
            print('Sorry for error') 
            #variable instantiation
#printer

            client.shutdown(socket.SHUT_RDWR)
            client.close() 
            break
#check for rand and ensure to move for better
#variable instantiation

def client_send():
    global state
    while True:
        #printer

        if state == 'INIT':
            #check for mover and foc

            continue 
        elif state == 'STOP':
            client.close()
            break
            #printer

        else:
            message = input('Enter new message:')
            client.send(message.encode('utf-8')) 
#printer

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
#check for mover and foc
def sigterm():
    global state
    print('SHUT DOWN client')
    state = 'STOP'
    client.close()
#check for mover and foc

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigterm)
