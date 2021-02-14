import socket
import time
import os

hostn = socket.gethostname()
ipad = socket.gethostbyname(hostn)

print ("ip address is:  " + ipad)
print ("ip class is your ip's 7 frist numbers")
ip = input("enter the ip class : ")

for i in range(1,256):

    try:
        live = gethostbyaddr(ip + str(i))
        print ("ip live: ",ip + str(i),live[0])


    except:

        print("_______")


