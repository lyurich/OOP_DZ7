# class FamilyTree:
#     pass


class FamilyTree:
    pass


from src.main.java.DZ7.Father import FamilyTree


class Father(FamilyTree):

    def __init__(self, type, name, age, height):
        self.type = type
        self.name = name
        self.age = age
        self.height = height


father = Father
ob = Father("Father", "Petr", 50, 180)
