# Kursovaya-ABS
## Риализованный функционал
* Реализован вход пользователя в приложения с помощою ввода логина и пароля
* Реализован вывод таблицы на форму пользователя

## Описание работы приложения
При запуске, открывается окно для ввода логина и пароля пользователя 

![](https://github.com/YUBobov/Kursovaya-ABS/blob/master/screenshots/LoginForm.PNG?raw=true)

После верного ввода логина и пароля, пользователю открывается окно, в котором он может ввести навзание таблицы и вывсти её на форму

![](https://github.com/YUBobov/Kursovaya-ABS/blob/master/screenshots/TableForm.PNG?raw=true)

Если таблица существует, на форму выводится информация из неё

![](https://github.com/YUBobov/Kursovaya-ABS/blob/master/screenshots/TablichaEst.PNG?raw=true)

Если таблицы не существует, пользователю выводится сообщение о несуществующей таблице

![](https://github.com/YUBobov/Kursovaya-ABS/blob/master/screenshots/TablichiNet.PNG?raw=true)

## Файлы с кодом проекта

### Серверная часть
* ![Файл с основными функциями сервера, служащий для соединния с клиентом через сокет](https://github.com/YUBobov/Kursovaya-ABS/blob/master/server/serv_con.py)
* ![Файл, выполняющий функции для работы с базой данных](https://github.com/YUBobov/Kursovaya-ABS/blob/master/server/bd_con.py)
* ![Main файл, обхединяющий оба предыдущих файла вместе для работы сервера](https://github.com/YUBobov/Kursovaya-ABS/blob/master/server/main.py)

### Клиентская часть
* ![Форма окна логина](https://github.com/YUBobov/Kursovaya-ABS/blob/master/klient/loginForm.py)
* ![Форм основного окна](https://github.com/YUBobov/Kursovaya-ABS/blob/master/klient/test1.py)
* ![Файл с основными функциями клиента, служащий для соединеия клиента с сервером через сокет](https://github.com/YUBobov/Kursovaya-ABS/blob/master/klient/sever.py)
* ![Файл, соединяющий все предыдущие файлы вместе для корректной работы приложения](https://github.com/YUBobov/Kursovaya-ABS/blob/master/klient/kli_conn.py)

