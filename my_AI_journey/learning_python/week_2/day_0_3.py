#from random import randint
#num= randint(1,10)
#guess= eval(input("Enter your guess: "))
#if guess==num:
#    print("You got it")
#else:
#    print("Sorry. The number is ", num)
grade= eval(input("Enter your score: "))
if grade>=80 and grade<90: 
    print("Your grade ia a B.")
if grade>=90:
    print("A")
if grade>=70 and grade<80:
    print("B")
if grade >=60 and grade<70:
    print("C")
if grade>=50 and grade<60:
    print("D")
if grade<50:
    print("F")
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")