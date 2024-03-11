import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="./server_cert.pem", keyfile="keyfile")


bindsocket = socket.socket()
bindsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
bindsocket.bind(('localhost', 6652))
bindsocket.listen(5)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        data = connstream.recv(1024)
        print(data)
        connstream.sendall(data)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
