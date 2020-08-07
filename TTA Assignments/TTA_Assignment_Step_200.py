


class Admiral:
    def __init__(self):
        self.__privateCode = 'password'

    def getPrivateCode(self):
        return(self.__privateCode)

    
class Cadet:
    def __init__(self):
        self._proectedCode = ''


def logIn():
    password = Cadet()
    password._protectedCode = 's%L9oK!Fv8eE'
    print("Welcome, Cadet Johnson.")
    password = Admiral()
    highSecurity = password.getPrivateCode()
    if highSecurity == 'password':
        print("Weclome, Admiral Smith.")
     


if __name__ == "__main__":
    logIn()
