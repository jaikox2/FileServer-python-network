import socket


host =socket.gethostname()
port = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

filename =input("Filename ? ->")
if filename != 'q':
    s.send(filename.encode('ascii'))
    data = s.recv(1024)
    
    if data != '':
        print(data.decode('ascii'))
        filesize = int(data)
        massage = input("File Exists,"+str(filesize)+\
                            "Byes, download ? (Y/N)? -> ")

        if massage == 'Y':
            OK ='OK'
            print(OK)
            s.send(OK.encode('ascii'))
            fo = open("new_"+filename, "wb")
            data = s.recv(filesize)
            fo.write(data);
            fo.close()
            print ("Download complete!")

        else:
            print("File does not Exists")

s.close()


    
