carSales = {"red": 10, "blue": 2, "silver": 8} #red is a key, 10 is the value

print(carSales["blue"])

carSales["blue"] =3
print(carSales["blue"])
#use in operator to see if a key is already associated

list(carSales.keys()) # returns the keys
list(carSales.values()) #returns all values
carSales["green"]=0

print(carSales)
