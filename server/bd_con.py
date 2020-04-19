import pymysql
def lod(login, password):
    con = pymysql.connect(host='localhost', user='debian', passwd='123', db='USERS', charset='utf8', use_unicode=True)
    cur_f = con.cursor()
    cur_f.execute("SELECT pass FROM login WHERE (name = '%s')" % login)
    tabl_f = cur_f.fetchone()
    if str(tabl_f[0]) == str(password):
        rezult = "true"
    else:
        rezult = "false"
    con.close()
    return rezult

def podkl(name):
    con = pymysql.connect(host='localhost', user='debian', passwd='123', db='kursovaya', charset='utf8', use_unicode=True)

    cur_f = con.cursor()
    cur_f.execute("show tables")
    tabl_f = cur_f.fetchall()
    stroka = ""
    if str(name) not in str(tabl_f):
        stroka +="Таблица " +  str(name) + " Не найдена"
        #cur_f.execute("CREATE TABLE %s (age INT, name varchar(20))" % name)
    else:

        stroka +="Таблица " + str(name) + "\n"
        cur_f.execute("SELECT * FROM %s" % name)
        for i in cur_f:
            stroka += str(i) + "\n"
    return stroka
    con.close()







