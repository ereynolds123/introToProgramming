#An adventure text based game

#Import necessary dependencies
import random

#Create character class
class Character():
    #Characters have a name, health, inventory
    def __init__(self, name, health, inventory, house):
        self.name = name
        self.health = health
        self.inventory = []
        self.house = house
    
    #Allows you to know the name of the character
    def getName(self):
        return self.name
    
    #A function to damage to the character
    def damage(self):
        self.health =self.health - 1
        print("Sorry {}. You have been hurt!. Your health is now {}".format(self.name, self.health))
    
    #def addToInventory(self, inventory):
        #self.inventory =self.inventory.append(inventory) #how do I get the inventory to append into the array on the class
        
    #Returns what is in the inventory    
    def getInventory(self):
        return self.inventory
    
    #Function to determine house by random chance
    def getHouse(self):
        if random.random() >  0.75:
            self.house = "Slytherine"
        elif random.random() <= 0.75 and random.random() >0.5 :
            self.house = "Ravenclaw"
        elif random.random() <= 0.5 and random.random() >0.25 :
            self.house = "Ravenclaw"
        else:
            self.house = "Gryffindor"
        
        print("Your house is {}".format(self.house))
        return self.house
    

def main():
    #Welcome message
    print("Welcome to the Harry Potter world. Try to survive against you enemies in Hogwarts. Choose your name, amount of damage you would like and see if you can survive.")
    
    #Get user inputs for the character and difficulty of play
    characterName = input("Enter your character's name : ")
    damageAmount = int(input("Enter a number 1-10 \n(1 being very difficult, 10 being very easy) for damage amount you can take : "))
    
    #Create the character
    character = Character(characterName, damageAmount, [], "")
    
    #First period of Hogwarts 
    def firstPeriod():
        #Print first class message
        print("Welcome {}. Take the train to Hogwarts. Meet Ron. Roll for damage.".format(character.getName()))
        #Breaks the text into next actions 
        breakPoint = input("Hit enter to continue")
        
        #If a random integer is < 0.3, the character takes one hit of damage
        if random.random() < 0.3:
            character.damage()
            breakPoint = input("Hit enter to continue")
            
        #Otherwise, the character adds chocolate to their inventory
        else:
            #character.addToInventory("Chocolate")
            print("Ron gives you chocolate. You thank him and join him for a chat.")
            breakPoint = input("Hit enter to continue")
        
    firstPeriod()
    
    #Second period of Hogwarts
    def secondPeriod():
        print("It's time to get sorted into houses. Roll to get into a house.")
        desireHouse = input("Enter which house you would like to get :")
        character.getHouse()
        breakPoint = input("Hit enter to continue")
        
    secondPeriod()

main()