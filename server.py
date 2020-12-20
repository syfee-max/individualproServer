import time, socket, sys, ssl
 
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 context = ssl.create_default_context()
port = 8080

  
new_socket.bind((host_name, port))
nnew_socket = context.wrap_socket(new_socket, s_ip )
print( "Binding successful!")
print("This is your IP: ", s_ip)
 
        
name = input('Enter name: ')
 
nnew_socket.listen(1) 
 
 
conn, add = nnew_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)