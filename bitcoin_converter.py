# Convert Bitcoin to Dollars

# prinn conversion statemtn
print("As of 1/15/2021 at 5:26 AM, Bitcoin is currently trading at $38, 508.73.")
#user inputs amount of bitcoin
bitcoinAmount = (int(input("How much Bitcoin do you own? Enter a number: ")))
#value of bitcoin calculated
bitcoinValue = (bitcoinAmount * 38508.72)
#transform bitcoin Value to string
bitcoinStr= str(bitcoinValue)
#print value of bitcoin
print("The is worth " + bitcoinStr + " US Dollars.")
