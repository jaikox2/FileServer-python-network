import socket
import threading
import os

def RetrFile(name,sock):
        filename = sock.recv(1024)
        if os.path.isfile(filename):
            print(os.path.getsize(filename))
            num=os.path.getsize(filename)
            sock.send(str((os.path.getsize(filename))).encode('ascii'))
            userResponse = sock.recv(1024)
            print(userResponse)
            if userResponse == b'OK':
                with open(filename, "rb") as f:
                    bytesToSend = f.read(num)
                    sock.send(bytesToSend)
                    
                    
        else:
            #sock.send("ERR")

        sock.close()


host = socket.gethostname()
port = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen(5)

print ("Server Started")

while True:
    c,addr = s.accept()
    print ("client connected ip :<" +str(addr)+">")
    t = threading.Thread(target = RetrFile, args=("retrThread",c))
    t.start()
s.close()


