from tkinter import ttk
from Controllers.UserController import UserController
from tkinter import *
from datetime import datetime, timedelta

from Views.NewPasswordView import NewPassword


class AuthView(Tk):
    '''
    класс для создания авторизации
    '''
    def __init__(self):
        super().__init__()
        self.title('ВХод в систему ОТель')
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
        self.button = ttk.Button(self,text='Войти в систему')
        self.button.pack(anchor='center')
        self.button["command"] = self.button_clicked
        #словарь для подсвета количества неправильных попыток вводя пароля
        self.count_error ={}

    def button_clicked(self):
        '''
        метод события при нажатии на кнопку
        :return: переход в другое окно или вывод сообщения
        '''
        #текс введенный в строку логин
        self.user_login = self.login_input.get()
        #ПЕРЕДАПТЬ ЛОГИН И ПАРОЛЬ
        self.user_password = self.password_input.get()
        # передать логин и пароль в метод auth
        self.user =UserController.auth(self.user_login,self.user_password)


        #если поля пустые
        if self.user_login == '' or self.user_password =='':
            self.message['text'] = 'введите логин и пароль'

        #проверка
        elif self.user:

            if self.user.ban:
                self.message['text']='ВЫ заблокированный. ОБратитесь к администратору'
            elif self.user.first_auth:
                #направить в другое окно
                self.message['text']='первый вход в систему'
                password= NewPassword(self.user.login)

            elif (datetime.now().date() - self.user.date_auth).days>=31:  #добавила date и days чтобы правильно работали между собой типы данных
                UserController.update(self.user.id, ban= 1)
            else:
                self.message['text']=f'ЗДравствуйте {self.user_login}'
                self.count_error[self.user_login]=0
                UserController.update(self.user.id, first_auth=datetime.now().date()) #обновитть дату авторизации на сегодня
                if self.user.role_id ==2:
                    #перейти в окна админа
                    pass

        else:
            self.message['text']=f'вы ввели неверный логин или пароль'

        #проверка введенного логина в бд
        self.test_user = UserController.show_login(self.user_login)
        if self.test_user is not None:
            #начало подсчета поппыток
            if self.user_login not in self.count_error:
                self.count_error[self.user_login]=0 #добавить в словарь ключ знаяение user0
            self.count_error[self.user_login]+=1
            if self.count_error[self.user_login]>3:
                UserController.update(self.test_user.id, ban=1)



if __name__=='__main__':
    window = AuthView()
    window.mainloop()
