from orm.core.connection import Connection
from settings import db_conection_settings as d


user = d['user']
password = d['password']
host = d['host']
database = d['database']
port = d['port']

class PrepareQuery:
    def __init__(self):
        self.query = query
        
#query = "insert into alumnos (matricula, nombre, apellido) values(34,'qweqwe', '222asd')"
#query = "create table pescados (nombre varchar(60), apellido varchar (50), id int primary key auto_increment)"

#query = "insert into pescados (nombre, apellido) values ('pescado2', 'apellido2');"
#query1 = "select * from pescados"
query = "select * from alumnos"


class RunQuery(Connection):
    def __init__(self,query, user, password,host,database, port,**kwargs):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.query = query

        self.conn()


    def conn(self):
        self.c = Connection(database=self.database, host=self.host, port=self.port)
        self.create_cursor()

    def create_cursor(self):
        self.cursor = self.c.cursor()
        self.execute_query()

    def execute_query(self):
        self.cursor.execute(self.query)
        self.c.commit()
        self.get_data()

    def get_data(self):
        for data in self.cursor:
            print(data)
        self.cursor.close()
        self.c.close()



RunQuery(query, user,password,host,database,port)



