from entities.mushroom import Mushroom
from Connection import connection as db

class MushroomDAO:
    # def __init__(self):
    #     db.connection = db.connection
        
    @staticmethod
    def insert(mushroom):
        mycursor = db.connection.cursor()
        sql = "INSERT INTO mushrooms (name, poisonous) VALUES (%s, %s)"
        values = (mushroom.GetName(),mushroom.GetPoisonous(),)
        mycursor.execute(sql, values)
        db.connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")
    
    @staticmethod
    def select():
        mycursor = db.connection.cursor()
        mycursor.execute("SELECT id_mushroom, name, poisonous FROM mushrooms")
        myresult = mycursor.fetchall()
        mushrooms = []
        for row in myresult:
            mushroom = mushroom(row[1], row[2], row[3], row[0])
            mushrooms.append(mushroom)
        return mushrooms
    
    @staticmethod
    def selectByName(name):
        mycursor = db.connection.cursor()
        mycursor.execute(("SELECT id_mushroom, name, poisonous FROM mushroom WHERE name LIKE %s"), (name,))
        row = mycursor.fetchone()
    
        if row:
            mushroom = Mushroom(name=row[1], poisonous=row[2], id_mushroom=row[0])
            return mushroom
        else:
            return None
        
    @staticmethod
    def selectPoisonous(name):
        mycursor = db.connection.cursor()
        mycursor.execute(("SELECT id_mushroom, name, poisonous FROM mushroom WHERE name LIKE %s"), (name,))
        row = mycursor.fetchone()
    
        if row:
            mushroom = Mushroom(name=row[1], poisonous=row[2], id_mushroom=row[0])
            return mushroom.GetPoisonous()
        else:
            return None
