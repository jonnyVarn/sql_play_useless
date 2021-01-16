import mysql.connector 
from time import sleep as sleep
from subprocess import Popen as cmd_run
import os
#nothing
if os.name.find("NT"):
    print("hello windows")
if os.name.find("BSD"):
    print("hello BSD")
    os_str=(cmd_run(["uname", "-a"]))
    print(os_str)
    sql_or_not=str(cmd_run(["which", "mysql"]))
    if sql_or_not.find("No"):
        print("mysql not installed")
        cmd_run(["pkg_add", "mariadb-server])

if os.name.find("linux"):
    print("hello linux")
    os_str=(cmd_run(["uname", "-a"]))
    print(os_str)

cmd_run(["uname"])
cmd_run(["which", "mysql"])
mydb= mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="bad_password",
        )

mycursor = mydb.cursor()
print("mysql -u root -p")
sleep(1)
print("CREATE DATABASE IF NOT EXISTS facebook")
# Put your non-Plugin stuff after this line
#create the database facebook if it does not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS facebook")
#create a user called facebook
try :
    mycursor.execute("CREATE USER 'facebook'@'localhost' IDENTIFIED BY 'bad_password' ")
except: 
    print("user already there or privilege error")

print("CREATE USER 'facebook'@'localhost' IDENTIFIED BY 'bad_password' ")
#grant user acess from anyhost to facebook
mycursor.execute("GRANT ALL PRIVILEGES ON facebook.* TO 'facebook'@'localhost'")
mycursor.execute("FLUSH PRIVILEGES")
#begin as facebook

#mydb =  mysql.connector.connect(
#        host="localhost",
#        user="facebook",
#        password="bad_password"
#        )
#mycursor= mydb.cursor()

mycursor.execute("USE facebook")
mycursor.execute("CREATE TABLE IF NOT EXISTS people(id INT AUTO_INCREMENT PRIMARY KEY, firstname varchar(100), lastname varchar(100), email varchar(200))")
mycursor.execute("CREATE TABLE IF NOT EXISTS friends(id INT AUTO_INCREMENT PRIMARY KEY, person1 INT, person2 INT, FOREIGN KEY (person1) REFERENCES people(id), FOREIGN KEY (person2) REFERENCES people(id))")

mycursor.execute("USE facebook")
#insert values to people
mycursor.execute("INSERT INTO people (firstname, lastname, email) values ('John', 'Doe', 'john.doe@doecompany.com')")
mycursor.execute("INSERT INTO people (firstname, lastname, email) values ('Amanda', 'Johansson', 'amanda.johansson@amanda.com')")
mycursor.execute("INSERT INTO people (firstname, lastname, email) values ('Jane', 'Sharp', 'jane.sharp@sharpcompany.com')")
mycursor.execute("INSERT INTO people (firstname, lastname, email) values ('David', 'Doe', 'david.doe@doecompany.com')")
mydb.commit()

# insert values to friends
mycursor.execute("INSERT INTO friends (person1, person2) values (4,1)")
mycursor.execute("INSERT INTO friends (person1, person2) values (4,2)")
mycursor.execute("INSERT INTO friends (person1, person2) values (3,1)")
mycursor.execute("INSERT INTO friends (person1, person2) values (2,3)")
mycursor.execute("INSERT INTO friends (person1, person2) values (2,4)")
mydb.commit()

#search for friends
#mycursor.execute("SELECT people.id, people.firstname FROM people RIGHT JOIN friends ON people.id = friends.id where friends person1 is not NULL")  



