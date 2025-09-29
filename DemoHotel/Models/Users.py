from Connection.connect import *
from Models.Roles import Roles


class Users(Model):
    #модель описывающая таблицу РОлей пользователя
    #id первичный ключ
    #login название роли с уникальным именем и количеством символов менее 100
    #password пароль
    #role_id свзяь с таблицей роли
    #ban блокировка пользователя
    #date_auth дата авторизации
    #first_auth первая авторизация

    id=PrimaryKeyField()
    login= CharField(unique=True, max_length=100)
    password= CharField()
    role_id= ForeignKeyField(Roles, backref='users')
    ban= BooleanField(default=False)
    date_auth= DateField(null=True)
    first_auth= BooleanField(default=True)


    class Meta:
        database= mysql_db

if __name__=="__main__":
    mysql_db.create_tables([Users]) #метод добавляет таблицу в базу данных
