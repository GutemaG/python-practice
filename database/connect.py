import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database="python",
)
cursor = db.cursor()
# cursor.execute("create database python")
# print(db)
# cursor.execute("show databases")
# databases=cursor.fetchall()

# print(databases) #this is befor adding database to conncet
# for database in databases:
# 	print(database)
# 	
#################Show tables#########
# cursor.execute("create table users(id int not null auto_increment primary key,name VARCHAR(255),user_name VARCHAR(255))")

# cursor.execute("desc users")
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
values=("Birhanu","Gutema")
# cursor.execute(query,values)
# tables=cursor.fetchall()
# print(tables)
# db.commit()
# values = [
#     ("Peter", "peter"),
#     ("Amy", "amy"),
#     ("Michael", "michael"),
#     ("Hennah", "hennah")
# ]
# cursor.executemany(query,values)
cursor.execute("select*from users")

# cursor.execute("delete from users where id>19")

users=cursor.fetchall()
print(users)
for user in users:
	print(user)

