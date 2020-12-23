import mysql.connector
from . models import *

class Db:
    def __init__(self):
        self.db_connection = mysql.connector.connect(user="root", password="MyNewPass", 
                                                host="localhost", database="facebook" )
        self.cursor = self.db_connection.cursor()

    def __del__(self):
        self.db_connection.close()

def login_db(user):
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


def insertLogin_db(id, user):
    db = Db()
    cursor = db.cursor
    sql = "INSERT INTO login VALUES(null, '"+user.username+"', '"+user.password+"',"+str(id)+")" 
    cursor.execute(sql)
    loign_id = cursor.lastrowid
    db.db_connection.commit()
    if loign_id:
        return loign_id
    else:
        return 0

    
def regsiter_db(user):
    db = Db()
    cursor = db.cursor    
    sql = "INSERT INTO users VALUES(null,'"+user.first_name+"', '"+user.last_name+"', '"+user.gender+"', '"+user.dob+"', '"+user.email+"', '"+user.phone+"' )" 
    cursor.execute(sql)
    user_id = cursor.lastrowid
    db.db_connection.commit()
    if user_id:
        return user_id
    else:
        return 0


# def update_password_db(username, current_password, new_password):
#     db = Db()
#     cursor = db.cursor    
#     sql = "SELECT * FROM login where username ='"+username+"'" 
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     if result
#         current_pass = result['password']
#         if current_pass == current_password

# Update password
# insert post
# delete post

#getters and setters
# https://www.python-course.eu/python3_properties.php
