import mysql.connector
from files.query import query_select


class Database:


    def connect_db(self):

        self.sql =  mysql.connector.connect(
                         host='sql7.freesqldatabase.com',
                         user='sql7814711',
                         password='x5bZR5U8vI',
                         database='sql7814711'
        )

        status = self.sql.is_connected()
        try:
            if status:
                print("✅ Conexão com o MySQL estabelecida com sucesso!",status)
                print('')

        except Error as e:
         print("❌ Erro ao conectar:", e)
         print('')

    def read_values(self):
         mycursor = self.sql.cursor()
         mycursor.execute(query_select)
         result = mycursor.fetchall()
         print(result)
         print('')


    def close_connection(self):
        self.sql.close()
        print('Connection was close')
        print('')



