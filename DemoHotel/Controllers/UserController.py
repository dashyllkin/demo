from Models.Users import Users
from datetime import datetime

class UserController:
    """
    Данный класс отвечает за функционал
    АУнтетификация
    Решистрация пользователя
    Изменение данных пользователя
    """
    #ВЫвод пользователя

    @classmethod
    def show_login(cls,login):
        """
        Метод вывода данных о пользователе
        :param login: вводится логин искомого пользователя
        :return: если логин найден, выводится объект иначе None
        """
        return Users.get_or_none(Users.login == login)

    @classmethod
    def add(cls,login,password,role_id=1,):
        """
        Метод регистрации пользователя
        :param login: логин пользователя
        :param password: пароль пользователя
        :param role_id: роль пользователяпо умолчанию 1-пользователь
        :return:
        """
        Users.create(login=login,password=password,role_id=role_id
                     )
    #универсальный метод
    @classmethod
    def update(cls, id, **fields):
        '''
        МЕтод обновления данных о пользователе
        :param id: Айди пользователя
        :param fields: выбор полей для изменения
        :return:
        '''
        for key,value in fields.items():
            Users.update({key:value}).where(Users.id==id).execute()

    @classmethod
    def auth(cls,login, password):
        '''
        Метод аутентификации
        :param login: ввести логин
        :param password: ввести пароль
        :return: Если логин есть в таблицу проверяется его пароль с введенным иначе возвращаетс False
        '''
        user = UserController.show_login(login)
        if user is not None:
            if user.password==password:

                return user
            else:
                return False
        else:
            return False
if __name__ == "__main__":
    print(UserController.show_login('user'))
    #UserController.add('user','111111')
    #UserController.update(1,login='USERRR',password='222222')
    #print(UserController.auth('USERRR','222222'))