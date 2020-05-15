from orm.core.connection import Connection
from settings import db_conection_settings as d


user = d['user']
password = d['password']
host = d['host']
database = d['database']
port = d['port']

a=Connection( database = database, port=port)

c=a.cursor()
c.execute("select * from alumnos")

for data in c:
    print(data)

a.close()