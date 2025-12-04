from entities.user import User
from entities.mushroom import Mushroom
from entities.images import Image
from entities.search import Mushroom
from Connection import connection as db

class UserDAO:
    def __init__(self):
        self.__connection = db.connection
        
    def insert(self, user):
        mycursor = self.__connection.cursor()
        sql = "INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s)"
        values = (user.GetName(),user.GetSurname(),user.GetEmail(),user.GetPassword(),)
        mycursor.execute(sql, values)
        self.__connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")

    def select(self):
        mycursor = self.__connection.cursor()
        mycursor.execute("SELECT id_user, name, surname, email FROM users")
        myresult = mycursor.fetchall()
        users = []
        for row in myresult:
            user = User(row[1], row[2], row[3], row[0])
            users.append(user)
        return users
