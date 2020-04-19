import socket
def srv_con():
    sock = socket.socket()
    sock.bind(('',9799))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected: ', addr)
    return conn

def srv_discon(conn):
    conn.close()
    print ('End')

def srv_work(conn):
    date = conn.recv(1024)
    print(date)
    return date.decode('utf-8')

def srv_snd(conn,date):
    conn.send(date)
