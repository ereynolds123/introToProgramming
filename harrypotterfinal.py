#An adventure text based game

#Import necessary dependencies
import random

#Create class enemies
class Enemy():
    def __init__(self, nameEnemy, probOfWin):
        self.nameEnemy= nameEnemy
        self.probOfWin= probOfWin
        
    def getEnemyName(self):
        return self.nameEnemy
    
    def getProb(self):
        return self.probOfWin
        


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
        if self.health > 0:
            print("Sorry {}. You have been hurt!. Your health is now {}".format(self.name, self.health))
        else:
            print("You lose. Goodbye.")
            quit()
   
    def gainHealth(self):
        self.health =self.health +1
        print("You are healed {}. Your health is now {}".format(self.name, self.health))
    
    def addToInventory(self, itemToAppend):
        self.inventory.append(itemToAppend)
        print("Your inventory is {}.".format(self.inventory))
        
    def getInventory(self):
        return self.inventory
        print("Your inventory is {}.".format(self.inventory))
    #Returns what is in the inventory    
    def getInventory(self):
        return self.inventory
        print("You are here. Your inventory is {}".format(self.inventory))
    
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
        breakPoint = input("Hit enter to continue.\n")
        
        #If a random integer is < 0.3, the character takes one hit of damage
        if random.random() < 0.3:
            character.damage()
            breakPoint = input("Hit enter to continue.\n")
            
        #Otherwise, the character adds chocolate to their inventory
        else:
            character.addToInventory("Chocolate")
            character.getInventory()
            print("Ron gives you chocolate. You thank him and join him for a chat.")
            breakPoint = input("Hit enter to continue.\n")
        
    firstPeriod()
    
    #Second period of Hogwarts
    def secondPeriod():
        print("It's time to get sorted into houses. Roll to get into a house.")
        desireHouse = input("Enter which house you would like to get :")
        character.getHouse()
        breakPoint = input("Hit enter to continue.\n")
        
    secondPeriod()
    
    #Third period of Hogwarts
    def thirdPeriod():
        #Create enemy Snape
        enemySnape = Enemy ("Snape", 0.4)
        
        #Print third period message
        print("You walk into potions class and encounter {}.".format(enemySnape.getEnemyName()))
        print("He takes an immediate disliking to you.")
        print("Roll for damage")
        breakPoint = input("Hit enter to continue.\n")
        
        #If a random number is greater than the enemies probability of damage, do damage
        if random.random() > enemySnape.getProb():
            character.damage()
        #Otherwise, walk away without damage
        else:
            print("You have walked away from {} unscathed. For now.".format(enemySnape.getEnemyName()))
    thirdPeriod()
    
    #Fourth Period of Hogwarts
    def fourthPeriod():
        #Print fourth period message
        print("You have had a tough semester. Go see Hagrid.")
        breakPoint = input("Hit enter to continue.\n")
        
        #If a random number is greater than 0.5, gain health and add an owl to your inventory
        if random.random() > 0.5:
            character.gainHealth()
            character.addToInventory("Owl")
            breakPoint = input("Hit enter to continue.\n")
        #Otherwise print message
        else:
            print("Nothing to see at Hagrids. Have a good fourth period")
            breakPoint = input("Hit enter to continue.\n")
    fourthPeriod()
    
    #Fifth period of Hogwarts
    def fifthPeriod():
        enemyDraco = Enemy("Draco", 0.5)
        
        print("Wondering the halls, you run into you enemy {}. He challenges you to a duel. Roll to see if you can defeat him.".format(enemyDraco.getEnemyName()))
        breakPoint = input("Hit enter to continue.\n")
        
        #If a random number is greater than the enemies probability of damage, do damage
        if random.random() > enemyDraco.getProb():
            character.damage()
        #Otherwise, walk away without damage
        else:
            print("You have won!.Stick your tongue out.")
            breakPoint = input("Hit enter to continue.\n")
            
    fifthPeriod()
    
    #Sixth period of Hogwarts
    def sixthPeriod():
        #Print message of triwizard tournament
        print("{}, you have unluckily been entered into the Triwizard tournament. Roll to see if you defeat the Tournament.".format(character.getName()))
        breakPoint = input("Hit enter to continue")
        
        #If the random number is greater than 0.3, win the Triwizard Tournament. Add the cup to inventory
        if random.random() > 0.3:
            character.addToInventory("Triwizard Tournament Cup")
            print("Congratulations {}! You have defeated the Triwizard Tournament.".format(character.getName()))
            breakPoint = input("Hit enter to continue.\n")
        #Otherwise, damage to your character   
        else:
            character.damage()
            breakPoint = input("Hit enter to continue.\n")
            
    sixthPeriod()
    
    #Seventh Period of Hogwarts
    def seventhPeriod():
        #Print seventh period message
        print("You have fallen in love. Ask Ginny for a kiss. Roll to see if she lets you.")
        breakPoint = input("Hit enter to continue.\n")
        
        #If random number is greater than 0.7 you kiss Ginny. Otherwise, you get damage
        if random.random() > 0.7:
            print("Congratulations, {}! You kissed Ginny!".format(character.getName()))
            character.gainHealth()
            breakPoint = input("Hit enter to continue.\n")
        else:
            character.damage()
            breakPoint = input("Hit enter to continue.\n")
    seventhPeriod()
    
    #Eigth period of Hogwarts
    def eigthPeriod():
        #Print eigth period message
        print("Time to play quidditch! Roll the dice to see if you catch the Golden Snitch.")
        breakPoint = input("Hit enter to continue.\n")
        
        #If random number is higher than 0.5, you win the Golden Snitch. Otherwise, print failure message
        if random.random()> 0.5:
            character.addToInventory("Golden Snitch")
            breakPoint = input("Hit enter to continue.\n")
        else:
            print("You lost{}. Draco laughs in your face.".format(character.getName()))
            breakPoint = input("Hit enter to continue.\n")
    eigthPeriod()
    
    #Ninth Period of Hogwarts
    def ninthPeriod():
        #Print ninth period message
        print("Dumblebore tragically dies in a battle with Voldemort. Roll the dice to see if you can take vengeance and win his horcrux.")
        
        if random.random() > 0.7:
            character.addToInventory("Horcrux")
            breakPoint = input("Hit enter to continue.\n")
        
        else:
            character.damage()
            breakPoint = input("Hit enter to continue.\n")
        
        
    ninthPeriod()
    def tenthPeriod():
        #Print tenth period message
        print("Time for the final battle with Voldemort. Your health is {}.".format(character.health))
        
        #Create Voldemort enemy
        voldemortEnemy = Enemy("Voldemort", 0.6)
        
        #If health is greater than 3, you have a 50% chance of defeating Voldemort
        if character.health > 3:
            if random.random() > voldemortEnemy.getProb():
                print("Congratulations {}! You win.".format(character.getName()))
                character.addToInventory("Trophy")
            else:
                print("{} defeated you. You lose!".format(voldemortEnemy.getEnemyName()))
                quit()
        #If health is less than 3, you have a 20% chance of defeating Voldemort
        else:
            if random.random()> 0.8:
                print("Congratulations {}! You win.".format(character.getName()))
                character.addToInventory("Trophy")
            else:
                print("{} defeated you. You lose!".format(voldemortEnemy.getEnemyName()))
                quit()
    
    tenthPeriod()
main()