import socket
import ssl

hostname = 'localhost'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("./client_CA.pem")


conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)

conn.connect((hostname,6652))

conn.sendall(b"HelloFriends")

data = conn.recv(1024)

print('Received', repr(data))
