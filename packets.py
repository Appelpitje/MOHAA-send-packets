import socket
import time

IP = "127.0.0.1"
port = 12203
cmd = "getstatus"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.8)

try:
    sock.connect((IP, port))
    sock.send("\xFF\xFF\xFF\xFF\x02" + cmd)
    received = sock.recv(65565)
    print(received)
    sock.close()
except:
    print("Connection timeout.")
    sock.close()