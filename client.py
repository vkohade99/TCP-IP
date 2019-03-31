import socket

s = socket.socket()
host = '192.168.228.129'
port = 9999

s.connect((host,port))
p,q = [int(i) for i in s.recv(2048).decode('utf-8').split('\n')]
print(p)
print(q)
output_str = str(p+q)
s.send(str.encode(output_str))

print(output_str)