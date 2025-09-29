from peewee import *
# Connect to a MySQL database on network.
mysql_db = MySQLDatabase(
    'OvcD1234_dem_ex',
     user='OvcD1234_dem1',
     password='11111',
     host='10.11.13.118',
     port=3306)
if __name__=="__main__":
    mysql_db.connect()