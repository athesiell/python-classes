class Field:
    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value
    
    def set_value(self, new_value):
        self.__value = new_value


field = Field()
print('Initial value:',field.get_value())
field.set_value(20)
print('New value:', field.get_value())