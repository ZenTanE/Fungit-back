class Image:
    def __init__(self, imageLink, idUser=None, idImage=None):
        self.__idImage = idImage
        self.SetImageLink(imageLink)
        self.SetIdUser(idUser)
    def GetImageLink(self):
        return self.__imageLink
    def SetImageLink(self, imageLink):
        self.__imageLink = imageLink
    def GetIdUser(self):
        return self.__idUser
    def SetIdUser(self, idUser):
        self.__idUser = idUser
    def GetIdImage(self):
        return self.__idImage