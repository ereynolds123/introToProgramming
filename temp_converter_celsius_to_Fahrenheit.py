# Convert Fahrenheit to Celsius

# Ask user to input what Fahrenheit they want to convert
# Compute conversion of inputed Fahrenheit to Celsius
# Output the converted value in Celsius
# Repeat 3 times

def convertFahrenheitToCelsius():
    fahrenheitInputToConvert= int(input("Enter temperature in F you wish to convert: "))
    convertFtoC= round((fahrenheitInputToConvert -32) / (1.800))
    print("The temperature in Celsius is " + str(convertFtoC) + " degrees.")
                    
    
for index in range(3):
        convertFahrenheitToCelsius()
