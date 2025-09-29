from tkinter import *
from tkinter import ttk
from Controllers.UserController import UserController
from datetime import datetime, timedelta
class NewPassword(Tk):
    '''
    Класс для создания окна изменения пароля
    '''
    def __init__(self,user): #передаем пользователя чтобы понять у кого менять пароль из предыдущего окна
        super().__init__()
        self.user = UserController.show_login(user)

        self.title('Изменение пароля')
        self.geometry('500x500')

        #старый пароль
        self.old_password = ttk.Label(self,text='введите старый паролЬ')
        self.old_password.pack(anchor='center')
        self.old_password_input=ttk.Entry(self)
        self.old_password_input.pack(anchor='center')

        #новый пароль
        self.new_password = ttk.Label(self, text='введите новый паролЬ')
        self.new_password.pack(anchor='center')
        self.new_password_input = ttk.Entry(self)
        self.new_password_input.pack(anchor='center')

        #повторить новый пароль
        self.second_new_password = ttk.Label(self, text='повторите новый пароль')
        self.second_new_password.pack(anchor='center')
        self.second_new_password_input = ttk.Entry(self)
        self.second_new_password_input.pack(anchor='center')

        # сообщение
        self.message = ttk.Label(self)
        self.message.pack(anchor='center')

        # кнопка ввода
        self.button = ttk.Button(self, text='Изменить пароль')
        self.button.pack(anchor='center')
        self.button["command"] = self.button_clicked

    def button_clicked(self):
        self.old_pass=self.old_password_input.get()
        self.new_pas=self.new_password_input.get()
        self.sec_new_pas=self.second_new_password_input.get()
        if not self.old_pass!='' or not self.new_pas !='' or not self.sec_new_pas!='':
            self.message['text'] = 'Поля должны быть заполнены'
        else:
            if self.old_pass==self.user.password:
                if self.new_pas==self.sec_new_pas:
                    UserController.update(self.user.id, password= self.new_pas, first_auth=0,date_auth=datetime.now().date())
                    self.destroy()
                else:
                    self.message['text']='Пароли не совпадают'
            else:
                    self.message['text'] = 'Вы ввели неверный пароль'


if __name__=="__main__":
    window=NewPassword('USERRR')
    window.mainloop()