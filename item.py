class Item:

    def __init__(self,name,description,weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return str((str(self.name) +" : " + str(self.description) + " ( " + str(self.weight) + "kg )"))
