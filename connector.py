import mysql.connector
import plac
from mysql.connector import errorcode


class conn:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root',
                                      password='anjums_786',
                                      database='chatbot', port=3306, host='localhost')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def checkemail(self,email):
        try:
            cursor = self.cnx.cursor()
            query = ("SELECT *  FROM users where email ='{}'" .format(email))
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            return len(results) > 0
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print ("Database does not exist")
            else:
                print(err)
    def signin(self,email,key):
        try:
            cursor = self.cnx.cursor()
            query = ("SELECT *  FROM users where users.email ='{}' and users.secretkey = {};" .format(email,key))
            cursor.execute(query)
            results = cursor.fetchall()
            return len(results) > 0
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print ("Database does not exist")
            else:
                print(err)
    def signup(self,email,username,key):
        try:
            cursor = self.cnx.cursor()
            query = ("INSERT INTO users (email,username,secretkey) VALUES (%s,%s,%s);")
            data = (email,username,str(key))
            print(query)
            cursor.execute(query,data)
            self.cnx.commit()
            return True
        except mysql.connector.Error as err:
            self.cnx.rollback()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print ("Database does not exist")
            else:
                print(err)
            return False
    def fetchoffers(self):
        try:
            cursor = self.cnx.cursor()
            query = ("SELECT *  FROM offers ")
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print ("Database does not exist")
            else:
                print(err)

