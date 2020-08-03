
class Item:
    skewNumber = int()
    quantity = int()
    departmentID = int()
    price = int()

    def itemFunction(self):
        msg = "\nAn item in the store."
        return msg

class Fruit(Item):
    fruitType = 'Mango'
    expirationDate = '21-8-2020'

    def itemFunction(self):
        msg = "\nA {} that is sold in the store.".format(self.fruitType)
        return msg

class Alcohol(Item):
    alcoholType = 'Rum'
    refrigerationNeeded = False

    def itemFunction(self):
        msg = "\nA container of {} that is sold in the store.".format(self.alcoholType)
        return msg
    
    
if __name__ == "__main__":
    item = Item()
    print(item.itemFunction())

    fruit = Fruit()
    print(fruit.itemFunction())

    alcohol = Alcohol()
    print(alcohol.itemFunction())
    
    
          
    
    
    
    


    

    
