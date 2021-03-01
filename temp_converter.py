# Convert Celsius temperature into Fahrenheit

# Create a function to convert Celsius to Fahrenheit
# Ask user to input what Celsius they want to convert
# Compute conversion of inputted Celsius to Fahrenheit
# Output the converted value in Fahrenheit
# Repeat 3 times

def convertCelsiusToFahrenheit():
    celsiusToConvertInput= int(input("Enter the temperature in C: "))
    tempInF = ((celsiusToConvertInput * 9/5 ) + 32)
    print("The temperature in Fahrenheit is " + str(tempInF) + " degrees")

for index in range(3):
    convertCelsiusToFahrenheit()
