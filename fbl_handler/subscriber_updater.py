from mysql.connector import MySQLConnection, Error
from dotenv import load_dotenv
import os
load_dotenv()

class SubscriberUpdater:

    def get_connection(self):
        return MySQLConnection.connect(host=os.getenv('emark_host'),
                                                 database=os.getenv('emark_database'),
                                                 user=os.getenv('emark_username'),
                                                 password=os.getenv('emark_password'))

    def unsubscribe_client(self, email: str):
        connection = None
        data_tuple = (email)
        try:
            connection = self.get_connection()
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                query = "UPDATE email_list_subscribers SET unsubscribed = UNIX_TIMESTAMP(now()), unsubscribeconfirmed=1 WHERE emailaddress = %s LIMIT 5"
                cursor = connection.cursor()
                cursor.execute(query, data_tuple)

                # accept the changes
                connection.commit()


        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")