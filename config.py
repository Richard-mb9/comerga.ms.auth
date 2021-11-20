import psycopg2
from src.utils.utils import getEnv

login_host = getEnv('pg_login_host')
login_user = getEnv('pg_login_user')
login_password = getEnv('pg_login_password')
login_port = getEnv('pg_login_port')

class PgLogin():
    def __init__(self):
        self.connection = psycopg2.connect(
            host=login_host,
            user=login_user,
            password=login_password,
            database='db_login'
        )
        self.cursor = self.connection.cursor()

    def insert(self, query):
        self.cursor.execute(query)
        return self.connection.commit()

    def select(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        records = self.cursor.fetchall()
        self.connection.close()
        columns = [desc[0] for desc in self.cursor.description]
        datas = []
        for item in records:
            i = 0
            data = {}
            for col in columns:
                data[col] = item[i]
                i +=1
            datas.append(data)
        return datas
