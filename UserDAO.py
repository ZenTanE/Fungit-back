from entities.user import User
from Connection import connection as db

class UserDAO:
    # def __init__(self):
    #     db.connection = db.connection
        
    @staticmethod
    def insert(user):
        mycursor = db.connection.cursor()
        sql = "INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s)"
        values = (user.GetName(),user.GetSurname(),user.GetEmail(),user.GetPassword(),)
        mycursor.execute(sql, values)
        db.connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")
    
    @staticmethod
    def select():
        mycursor = db.connection.cursor()
        mycursor.execute("SELECT id_user, name, surname, email FROM users")
        myresult = mycursor.fetchall()
        users = []
        for row in myresult:
            user = User(row[1], row[2], row[3], row[0])
            users.append(user)
        return users
