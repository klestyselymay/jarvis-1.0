import socket
from threading import Thread

# server's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    while True:
        with open('url.txt') as f:
            url = f.read()
        if url == '':
            False
        else:
            cs.send(url.encode())
            with open('url.txt', 'w') as f2:
                f2.write('')

        with open('app.txt') as f3:
            app1 = f3.read()
        if app1 == '':
            False
        else:
            cs.send(app1.encode())
            with open('app.txt', 'w') as f4:
                f4.write('')

        with open('pyperclip.txt')as cpl1:
            clp1 = cpl1.read()
        if clp1 == '':
            False
        else:
            cs.send(clp1.encode())
            with open('pyperclip.txt', 'w')as cpl2:
                cpl2.write('')

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()