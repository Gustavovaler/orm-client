from orm.core.connection import Connection
from settings import db_conection_settings as d


user = d['user']
password = d['password']
host = d['host']
database = d['database']
port = d['port']
query = "select * from employees limit 2"



class RunQuery(Connection):
    def __init__(self,query, user, password,host,database, port,**kwargs):
        # super().__init__()
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
        self.get_data()

    def get_data(self):
        for data in self.cursor:
            print(data)
        self.cursor.close()



RunQuery(query, user,password,host,database,port)



