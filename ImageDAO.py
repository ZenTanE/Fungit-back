from entities.images import Image
from Connection import connection as db

class ImageDAO:

    @staticmethod
    def insert(image):
        mycursor = db.connection.cursor()
        sql = "INSERT INTO images (image_link, id_user) VALUES (%s, %s)"
        values = (image.GetImageLink(), image.GetIdUser(),)
        mycursor.execute(sql, values)
        db.connection.commit()
        return (f"Se han añadido {mycursor.rowcount} valores")

    @staticmethod
    def select(images=[]):
        pass