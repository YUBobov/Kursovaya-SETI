import bd_con
import serv_con
con = serv_con.srv_con()
while True:
    com, date = serv_con.srv_work(con)
    print(com, date)
    if com == "work":
        name = bd_con.podkl(date)
        serv_con.srv_snd(con, name)

    elif com == "login":
        date = date.split(" ")
        rezult = bd_con.lod(date[0],date[1])
        print(rezult)
        serv_con.srv_snd(con, rezult)

    elif com == "close ":
        break

    else:
        print("error")
        break

serv_con.srv_discon(con)




# import asyncio
# import bd_con
# import socket
# import serv_con
# con, name= serv_con.serv()
#serv_con.serv()
#print(name)
#snd = bd_con.podkl(name)
#print(con)
#con.send(name.encode())
#con.close()
