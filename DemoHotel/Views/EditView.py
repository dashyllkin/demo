from tkinter import ttk
from Controllers.UserController import UserController
from tkinter import *
from datetime import datetime, timedelta

from Views.NewPasswordView import NewPassword
from Views.AdminView import AdminView


class EditView(Tk):
    '''
    класс для создания авторизации
    '''
    def __init__(self,login):
        super().__init__()
        self.user=UserController.show_login(login)

        self.title(f'Изменение пользователя {self.user.login} системы')
        self.geometry('500x200')
        #логин
        self.login = ttk.Label(self, text='Введите логин')
        self.login.pack(anchor='center')
        #строка ввода логина
        self.login_input = ttk.Entry(self)
        self.login_input.pack(anchor='center')
        #пароль
        self.password = ttk.Label(self, text='Введите пароль')
        self.password.pack(anchor='center')
        #строка ввода пароля
        self.password_input = ttk.Entry(self)
        self.password_input.pack(anchor='center')
        #сообщение
        self.message = ttk.Label(self)
        self.message.pack(anchor='center')
        #кнопка ввода
        self.button = ttk.Button(self,text='Изменить данные пользователя')
        self.button.pack(anchor='center')
        self.button["command"] = self.button_clicked
        #словарь для подсвета количества неправильных попыток вводя пароля
        self.count_error ={}

        #кнопка блокировать/разблокировать
        self.button_ban=ttk.Button(self,text='БЛокировать/Разблокировать')
        self.button_ban.pack(anchor='center')
        self.button_ban["command"] = self.button_banan

        #вернуться в админ панель
        self.button_exit=ttk.Button(self,text='вернуться в панель администратора')
        self.button_exit.pack(anchor='center')
        self.button_exit['command']=self.exit

    def button_clicked(self):
        '''
        метод события при нажатии на кнопку
        :return: переход в другое окно или вывод сообщения
        '''
        #текс введенный в строку логин
        self.user_login = self.login_input.get()
        #ПЕРЕДАПТЬ ЛОГИН И ПАРОЛЬ
        self.user_password = self.password_input.get()


        if self.user_login!='':
            UserController.update(self.user.id,login=self.user_login)
        if self.user_password!='':
            UserController.update(self.user.id,password=self.user_password)

    def button_banan(self):
        ban=self.user.ban
        print(ban)
        ban=not ban
        print(ban)
        UserController.update(self.user.id,ban=ban)

    def exit(self):



if __name__=='__main__':
    window = EditView('admin')
    window.mainloop()