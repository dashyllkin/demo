from tkinter import ttk
from Controllers.UserController import UserController
from tkinter import *
from datetime import datetime, timedelta

class AdminView(Tk):
    '''
    класс для создания панели администратора
    '''
    def __init__(self):
        super().__init__()


        self.title('Панель администратора')
        self.geometry('800x500')

        ##########раздел добавления пользователя#################
        self.add_frame = ttk.Frame(
            self,
            borderwidth=1,
            relief=SOLID,
            padding=[8,10]
        )
        self.add_frame.pack(
            anchor="center",
            fill=X,
            padx= 10,
            pady=10
        )
        self.add_title=ttk.Label(self.add_frame,text='Добавление новых пользователей')
        self.add_title.pack()

        # логин
        self.login = ttk.Label(self.add_frame, text='Введите логин')
        self.login.pack(anchor='center')
        # строка ввода логина
        self.login_input = ttk.Entry(self.add_frame)
        self.login_input.pack(anchor='center')
        # пароль
        self.password = ttk.Label(self.add_frame, text='Введите пароль')
        self.password.pack(anchor='center')
        # строка ввода пароля
        self.password_input = ttk.Entry(self.add_frame)
        self.password_input.pack(anchor='center')



        # сообщение
        self.message = ttk.Label(self.add_frame)
        self.message.pack(anchor='center')
        # кнопка ввода
        self.button = ttk.Button(self.add_frame, text='Добавить пользователя в систему')
        self.button.pack(anchor='center')
        self.button["command"] = self.button_clicked

        ############таблица с пользователями#######################
        columns=('login','password','ban')
        self.users=ttk.Treeview(self,columns=columns,show='headings')
        self.users.pack(fill=BOTH,expand=1)
        self.table()
        self.users.bind('<<TreeviewSelect>>',self.item_selected)


        #кнопка обновить
        self.button_update=ttk.Button(self,text='ОБновить таблицу')
        self.button_update['command']=self.table
        self.button_update.pack(anchor="center",expand=1)



    def table(self):
        #очистить таблицу
        for item in self.users.get_children():
            self.users.delete(item)
        list=UserController.get()
        users_list=[]
        for user in list:
            ban=''
            if user.ban:
                ban='Да'
            else:
                ban='Нет'
            users_list.append(
                (user.login,user.password,ban)
            )

        #добавить шапку таблицы
        self.users.heading('login',text='Логин')
        self.users.heading('password', text='Пароль')
        self.users.heading('ban', text='Заблокирован')
        for person in users_list:
            self.users.insert("", END,values=person)


    def button_clicked(self):
        '''
        метод события при нажатии на кнопку
        :return: переход в другое окно или вывод сообщения
        '''
        # текс введенный в строку логин
        self.user_login = self.login_input.get()
        # ПЕРЕДАПТЬ ЛОГИН И ПАРОЛЬ
        self.user_password = self.password_input.get()

        # если поля пустые
        if self.user_login == '' or self.user_password == '':
            self.message['text'] = 'введите логин и пароль'

        # проверка на пользователя с таким же логином
        elif UserController.show_login(self.user_login):
            self.message['text']='Пользователь с таким логином уже существует'
        else:
            UserController.add(self.user_login,self.user_password)

        #метод на событие выбора пользователя
    def item_selected(self,event):
        self.item=self.users.selection()[0] #получить строку
        self.user_data=self.users.item(self.item,'values')[0]

        print(f'Выбран {self.user_data}')

if __name__=='__main__':
    window = AdminView()
    window.mainloop()
