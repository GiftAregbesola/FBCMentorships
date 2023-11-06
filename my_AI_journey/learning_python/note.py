temp= eval(input("Enter a tempersture in Celsius: "))
f_temp= 9/5*temp+32
print("InFahrenheit, that is",f_temp)
if f_temp > 212:
    print("That temperature is above the boiling point.")
if f_temp < 32:
    print("That tempersture is below the freezing point.")