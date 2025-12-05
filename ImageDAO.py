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
    def select(image=None):
        mycursor = db.connection.cursor()
        if image is None:
            mycursor.execute("SELECT image_link, id_user, id_image FROM images")
            myresult = mycursor.fetchall()
            images = []
            for row in myresult:
                image = Image(row[1], row[2], row[0])
                images.append(image)
        else:
            sql = ("SELECT image_link, id_user, id_image FROM images WHERE image_link LIKE %s")
            values = (image.GetImageLink(),)
            mycursor.execute(sql, values)
            myresult = mycursor.fetchall()
            images = []
            for row in myresult:
                image = Image(row[1], row[2], row[0])
                images.append(image)
        return images