from entities.mushroom import Mushroom
from Connection import connection as db

class MushroomDAO:
    # def __init__(self):
    #     db.connection = db.connection
        
    @staticmethod
    def addMushroom(mushroom):
        mycursor = db.connection.cursor()
        sql = "INSERT INTO mushrooms (name, poisonous) VALUES (%s, %s)"
        values = (mushroom.GetName(),mushroom.GetPoisonous(),)
        mycursor.execute(sql, values)
        db.connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")
    
    @staticmethod
    def readMushroom(name=None):
        if name is None:
            mycursor = db.connection.cursor()
            mycursor.execute("SELECT id_mushroom, name, poisonous FROM mushrooms")
            myresult = mycursor.fetchall()
            mushrooms = []
            for row in myresult:
                mushroom = mushroom(row[1], row[2], row[3], row[0])
                mushrooms.append(mushroom)
        else:
            mycursor = db.connection.cursor()
            mycursor.execute(("SELECT id_mushroom, name, poisonous FROM mushrooms WHERE name LIKE %s"), (name,))
            row = mycursor.fetchone()
            mushrooms = []
            for row in myresult:
                mushroom = mushroom(row[1], row[2], row[3], row[0])
                mushrooms.append(mushroom)
        return mushrooms
        
    @staticmethod
    def removeMushroom(name):
        mycursor = db.connection.cursor()
        sql = "DELETE FROM mushrooms WHERE name = %s"
        values = (name,)
        mycursor.execute(sql, values)
        db.connection.commit()
        return (f"Se han eliminado {mycursor.rowcount} valores")
        
    @staticmethod
    def selectPoisonous(name):
        mycursor = db.connection.cursor()
        mycursor.execute(("SELECT id_mushroom, name, poisonous FROM mushrooms WHERE name LIKE %s"), (name,))
        row = mycursor.fetchone()
    
        if row:
            mushroom = Mushroom(name=row[1], poisonous=row[2], id_mushroom=row[0])
            return mushroom.GetPoisonous()
        else:
            return None
