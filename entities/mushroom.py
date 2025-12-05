class Mushroom:
    def __init__(self, name, poisonous, idMushroom=None):
        self.__idMushroom = idMushroom
        self.SetName(name)
        self.SetPoisonous(poisonous)
    def GetName(self):
        return self.__name
    def SetName(self, name):
        self.__name = name
    def GetPoisonous(self):
        return self.__poisonous
    def SetPoisonous(self, poisonous):
        self.__poisonous = poisonous
    def GetIdMushroom(self):
        return self.__idMushroom
