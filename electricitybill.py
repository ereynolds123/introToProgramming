# Determining electricity for bill
# 31.5 C/kwh on peak
# 7.4 c/kwh off peak
# 120 on peak hours
# 80 off peak hours
# Multiply on peak hours by on peak hours cost
# Multiply off peak hours by off peak hours
# Convert c value to dollas by dividing the total by 100

onPeakChargeInCents= 31.5 * 120
offPeakChargeInCents= 7.4 * 80 
totalChargeInDollars = ((onPeakChargeInCents + offPeakChargeInCents)/100)
print(totalChargeInDollars)

#Making the code modular
onPeakHours = int(input("How many hours did you have on Peak electricity hours? "))
onPeak= 31.5 * onPeakHours
offPeakHours = int(input("How many hours did you have off Peak electricity hours?"))
offPeak = 7.4 * offPeakHours
totalChargeInDollars = ((onPeak + offPeak)/100)
roundedCharge=round(totalChargeInDollars, 2)
print(roundedCharge)