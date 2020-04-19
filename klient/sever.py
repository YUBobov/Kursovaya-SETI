import socket

def srv_conn():
    sock = socket.socket()
    sock.connect(('192.168.42.128', 9799))
    return  sock

def srv_snd(sock, com, msg):
    #com+=" "
    sock.send(com.encode())
    sock.send(msg.encode())


def srv_rec(sock):
    data = sock.recv(1024)
    return data.decode('utf-8')

def srv_clos(sock):
    sock.close()