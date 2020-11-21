
import MySQLdb
from . data import *

class Db:
    def __init__(self):

        self.db_connection = MySQLdb.connect(user="root", password="", host="localhost", database="facebook" )
        self.cursor = self.db_connection.cursor()
        # db_commit = db_connection.commit()




def login_model(user):
    db = Db()
    cursor = db.cursor

    sql = "SELECT * FROM login WHERE username = '"+user.username+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        if result[2] == user.password:
            return('Login success')
        else:
            return('Incorrect password')
        
    
        print(result)
    else:
        return('username doesnot exist')

def insertLogin_model(user):
    db = Db()
    cursor = db.cursor
    # sql1 = "SELECT * FROM registration"
    # cursor.execute(sql1)
    # result = cursor.fetchall()
    # print(result)
    
    sql = "INSERT INTO login VALUES('','"+user.username+"', '"+user.password+"')" 
    cursor.execute(sql)
    db.db_connection.commit()



def regsiter_model(user):
    db = Db()
    cursor = db.cursor
    # sql1 = "SELECT * FROM registration"
    # cursor.execute(sql1)
    # result = cursor.fetchall()
    # print(result)
    
    sql = "INSERT INTO registration VALUES('','"+user.first_name+"', '"+user.last_name+"', '"+user.gender+"', '"+user.dob+"', '"+user.email+"', '"+user.phone+"' )" 
    cursor.execute(sql)
    db.db_connection.commit()
    
   
    
        


     


     
     
    


     
#        sql = “SELECT * FROM tbl_products WHERE product_id < 4”
# cursor.execute(sql)
# results = cursor.fetchall() 
# for row in results: 
# id = row[0] 
# name = row[1] 
# description = row[2] 
# print("Product id: %d, Product Name: %s, Description: %d " % (id, name, description))



"""
CREATE TABLE login(
    loginid int PRIMARY KEY AUTO_INCREMENT, 
    username varchar(100) UNIQUE, 
    password varchar(100) NOT NULL
    );
"""










