from Connection.connect import *


class Roles(Model):
    #модель описывающая таблицу РОлей пользователя
    #id первичный ключ
    #name название роли с уникальным именем и количеством символов менее 100
    id=PrimaryKeyField()
    name= CharField(unique=True, max_length=100)

    class Meta:
        database= mysql_db

if __name__=="__main__":
    mysql_db.create_tables([Roles]) #метод добавляет таблицу в базу данных