class Father:
    pass


from src.main.java.DZ7.Son import Father
# import Father


class Son(Father):

    def __init__(self, type, name, age, height):
        self.type = type
        self.name = name
        self.age = age
        self.height = height


son = Son
ob1 = Son("Son", "Igor", 15, 156)