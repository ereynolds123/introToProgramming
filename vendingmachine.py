# A program to calculate the components of a vending machine

#I got stuck on this one in a few parts. 


#Import json compiler
import json


#Create a Machine Status 
def MachineStatus():
    def __init__(self):
        #Initialize all values to 0
        self.vendingMachineLabel=lable
        self.totalAmountPreviouslyStocked =0
        self.totalAmountInStock = 0
        self.incomeFromLastStock = 0
        
    #Get the name of the machine
    def getMachineName( self ):
        return self.vendingMachineLabel
    
    #Gives a representation of the machine object 
    def __repr__( self ):
        return "Machine Label:{}, Previously Stocked:{} In Stock:{} Income From Last Stock:{}".format(self.vendingMachineLabel, self.totalAmountPreviouslyStocked,self.totalAmountInStock, self.incomeFromLastStock)

#Create an inventory item class
class InventoryItem:
    def __init__( self, itemName ):
        self.name = itemName
        #The amount stocked last
        self.totalStocked = 0
        #The amount in stock
        self.totalInStock = 0
        #The total number of slots
        self.totalSlots = 0
    #The amount to add to fully stock is the total last stocked plus a stock amount    
    def addToStocked( self, stockAmt ):
        self.totalStocked = self.totalStocked + stockAmt
    #The total amount stocked is the total in stock plus a stock amount    
    def addToInStock( self, inStockAmt ):
        self.totalInStock = self.totalInStock + inStockAmt
    #Total amount of slots    
    def incrementSlots( self ):
        self.totalSlots = self.totalSlots + 1
    #Determines the number sold of a soda
    def getNumberSold( self ):
        return self.totalStocked - self.totalInStock
    #Determine the percent sold of a soda
    def getSoldPct( self ):
        return self.getNumberSold() / self.totalStocked
    #The total amount needed to stock
    def getStockNeed( self ):
        return 8 * self.totalSlots - self.totalInStock
    #Get the name of the soda
    def getName( self ):
        return self.name
    #Determines the amount in stock
    def getNumberInStock( self ):
        return self.totalInStock
    #Gives a representation of the soda object 
    def __repr__( self ):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format( self.name, self.totalInStock, self.totalStocked, self.totalSlots )

def main():
    #Files names
    inventoryFileNames = ["REID_1F_20171004.json", "REID_2F_20171004.json", "REID_3F_20171004.json"]
    #Create a blank object to initialize
    itemNameToInventoryItem = {}
    machineObject ={}
    
    #For every file
    for inventoryFileName in inventoryFileNames:
        #Open the file
        inventoryFile = open( inventoryFileName, 'r' )
        #Convert the file into a json string
        inventoryData = json.loads( inventoryFile.read() )
        #The string is the contents of the json file 
        contents = inventoryData['contents']
        #Get the name of the machine
        machineLabel=inventoryData["machine_label"]
        print(machineLabel)
        # Add the machine label to a the Machine Status Class
        machineItem = machineObject.get(machineLabel, MachineStatus())
        
        #Add to the dictionary
        #machineItem.getMachineName() #Not sure what to add, need to add the label to the MachineStatus
        #print(repr(machineObject))
        
        #For each row in the json file
        for row in contents:
            #For every slot in the vending maching
            for slot in row['slots']:
                #Get the item name
                itemName = slot['item_name']
                #Create an instance of the inventory item if it doesn't exist
                inventoryItem = itemNameToInventoryItem.get( itemName, InventoryItem( itemName ) )
                
                #Add to the dictionary what needs to be stocked, what was stocked, and increment the slots
                inventoryItem.addToStocked( slot['last_stock'] )
                inventoryItem.addToInStock( slot['current_stock'] )
                inventoryItem.incrementSlots();
                
                itemNameToInventoryItem[itemName] = inventoryItem
            #Add slot["last_stock"] to Machine Status
            #Add ["current_stock"] to Machine Status
        #Income from last stocked function
            # Slots* (last_stocked -current_stock)
            
    #Create a list 
    inventoryItemsList = list( itemNameToInventoryItem.values() )
    
    #Create a machine list
    
    #Input your sort choice
    sortChoice =input("Would you you like the (m)achine report or the (i)nventory report? ")
    #If the choice is machine report print the machine report
    if sortChoice == 'm':
        print("Label      Pct Sold    Sales Total")
    #Have the user input their choice
    elif sortChoice =="i":
        sortChoice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
        
        # Sort by the appropriate input
        if sortChoice == 'n':
            inventoryItemsList.sort( key=InventoryItem.getName )
        elif sortChoice == 'p':
            inventoryItemsList.sort( key=InventoryItem.getSoldPct )
            inventoryItemsList.reverse()
        elif sortChoice == 's':
            inventoryItemsList.sort( key=InventoryItem.getStockNeed )
            inventoryItemsList.reverse()
       
        #print out the sorted item list
        print( 'Item Name            Sold     % Sold     In Stock Stock needs')
        for item in inventoryItemsList:
            print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
        print()
    
main()
