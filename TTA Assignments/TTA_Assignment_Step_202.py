

from abc import ABC, abstractmethod
class Aircraft(ABC):
    def propulsion(self, propType):
        print("Your propulsion type is",propType)
    @abstractmethod
    def propDesc(self, propType):
            pass

class Helicopter(Aircraft):
    def  propDesc(self, propType):
        print("The {} allow for hovering and precise manuevers.".format(propType))

def searchAndRescue():
    rescueEnvi = 'mountains' #would be a user input calling another function with a few different options
    if rescueEnvi == 'mountains':
        vehicle = Helicopter()
        vehicle.propulsion("over head rotors")
        vehicle.propDesc("over head rotors")

if __name__ == "__main__":
    searchAndRescue()
