class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #getters and setters, username and password -make it as private variables


class User:
    def __init__(self, first_name, last_name, gender, dob, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
   

        #getters and setters



#         CREATE TABLE registration(registerID int PRIMARY KEY AUTO_INCREMENT, first_name varchar(100), last_name varchar(100), 
# gender varchar(50), dob date, email varchar(100), phone varchar(100), username varchar(100) NOT NULL UNIQUE, password varchar(100) NOT NULL);

# INSERT INTO registration VALUES(1, 'Anu', 'Krishna', 'female', '2000-09-06', 'anu@gmail.com', '9090876543');