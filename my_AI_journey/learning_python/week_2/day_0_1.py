num1= eval(input("Enter the first number: "))
num2= eval(input("Enter the second number: "))
print("The average of the numbers you entered is" , ((num1+num2)/2))
num= eval(input("Enter a number: "))
print("Your number squared is ", num*num)
temp= eval(input("Enter a tempersture in Celsius: "))
f_temp= (9/5)*temp+32
print("In Fahrenheit, that is ", f_temp)
if f_temp>212:
    print("That temperature is above the boiling point.")
if f_temp<32:
    print("That temperature is below the freezing point.")
for i in range(10):
    print("*"*(i+1))
