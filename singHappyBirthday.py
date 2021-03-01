#Generic Happy birthday song

def singBirthday():
    print("Happy Birthday to you!")
    
def singToPerson(person):
    singBirthday()
    singBirthday()
    print("Happy birthday, dear " + person+".")
    singBirthday()
    print("\n")
    
singToPerson("Alice")
singToPerson("Mark")
singToPerson("Emily")

#Refactored

def happy():
    return "Happy birthday to you! \n"

def verseFor(person):
    lyrics= happy()* 2 + "Happy birthday, dear "+ person +".\n"+ happy()
    return lyrics

def main():
    for person in ["Fred", "Emily", "Lucy"]:
        print(verseFor(person))
main()