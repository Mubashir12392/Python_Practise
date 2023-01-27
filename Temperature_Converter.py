
#celsius to Fahrenheit
celsius_to_fahrenheit =int(input("Temperature in Your Area (Celsius):"))
#(0* C * 9/5) +32 = 32* F

Fahrenheit= (celsius_to_fahrenheit * 9/5) +32
print(f"{Fahrenheit} Fahrenheit")

#Fahrenheit to Celcius
Fahrenheit_to_Celsius= int(input("Temperature in your area (Fahrenheit):"))
# (32*F - 32) * 5/9 = 0*C
Celsius = (Fahrenheit_to_Celsius - 32) * 5/9
print(f"{Celsius} Celsius")

