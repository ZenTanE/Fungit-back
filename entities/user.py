class User:
    def __init__(self, name, surname, email, password, idUser=None):
        self.__idUser = idUser
        self.SetName(name)
        self.SetSurname(surname)
        self.SetEmail(email)
        self.SetPassword(password)
    def GetName(self):
        return self.__name
    def SetName(self, name):
        self.__name = name
    def GetSurname(self):
        return self.__surname
    def SetSurname(self, surname):
        self.__surname = surname
    def GetEmail(self):
        return self.__email
    def SetEmail(self, email):
        self.__email = email
    def GetPassword(self):
        return self.__password
    def SetPassword(self, password):
        self.__password = password
    def GetIdUser(self):
        return self.__idUser