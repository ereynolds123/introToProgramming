#Madlib maker
firstNoun =input("Enter a noun: ")
secondNoun= input("Enter a second noun: ")
firstVerb = input("Enter a verb: ")
firstAdverb =input("Enter and adverb: ")

# Create the lyrics to the madlib
madlibLines = "I'm just a {0}. \nI'm looking for a {1}.\nA {0} who knows how to {3},\nWithout even {4} off."

print("\n"+ madlibLines.format(firstNoun, secondNoun, firstNoun, firstVerb, firstAdverb))