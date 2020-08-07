


class Admiral:
    def __init__(self):
        self.__privateCode = 'password'

    def getPrivateCode(self):
        print(self.__privateCode)

    
class Cadet:
    def __init__(self):
        self._proectedCode = ''

user = Cadet()
user._protectedCode = 's%L9oK!Fv8eE'
print(user._protectedCode)

user = Admiral()
user.getPrivateCode()




