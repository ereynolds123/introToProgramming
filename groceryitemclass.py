class GroceryItem:
    def __init__(self, name, id, price):
        self.name = name
        self.id=id
        self.price = price

    def priceForNPurchases(self, numOfPurchases ):
        return self.price * numOfPurchases
        
def main():
    burritoGroceryItem = GroceryItem ("burrito", 241, 4.99)
    print(burritoGroceryItem.name)
    print(burritoGroceryItem.id)
    print(burritoGroceryItem.price)
    print(burritoGroceryItem.priceForNPurchases(4))
    
    print(burritoGroceryItem)
main()
        