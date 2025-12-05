class Search:
    def __init__(self, idUser, idMushroom):
        self.SetIdUser(idUser)
        self.SetIdMushroom(idMushroom)
    def GetIdUser(self):
        return self.__idUser
    def SetIdUser(self, idUser):
        self.__idUser = idUser
    def GetIdMushroom(self):
        return self.__idMushroom
    def SetIdMushroom(self, idMushroom):
        self.__idMushroom = idMushroom