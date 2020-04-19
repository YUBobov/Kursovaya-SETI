from PyQt5 import QtWidgets, uic
from test1 import Ui_Dialog
from loginForm import Ui_LogDialog
import sever
import  sys
#Инициализация окна
class mywin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    #Функция работы кнопки
    def btnClicked(self):
        jopa = self.ui.lineEdit.text()
        msg = "work"
        #Вызывается метод, которые принимает переменную
        sever.srv_snd(sock, msg, jopa)
        #Возвращает таблицу, если она есть
        self.ui.label.setText(sever.srv_rec(sock))

    #
    def closeEvent(self, event):
        jopa = " "
        msg = "close"
        sever.srv_snd(sock, msg, jopa)
        sever.srv_clos(sock)

#
class lgwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(lgwin,self).__init__()
        self.ui = Ui_LogDialog()
        self.ui.setupUi(self)
        #Переключаем поле ввода пароля в режим для ввода пароля
        self.ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        btn_log = self.ui.lineEdit_log.text()
        btn_pas = self.ui.lineEdit_pass.text()
        date = btn_log + " " + btn_pas
        msg = "login"
        sever.srv_snd(sock, msg, date)
        rez = sever.srv_rec(sock)
        if rez == 'true':
            self.close()
            self.main = mywin()
            self.main.show()



def main():
    global sock
    sock = sever.srv_conn()
    appp = QtWidgets.QApplication(sys.argv)
    logapp = lgwin()
    logapp.show()
    sys.exit(appp.exec_())



if __name__ == "__main__":
    main()
