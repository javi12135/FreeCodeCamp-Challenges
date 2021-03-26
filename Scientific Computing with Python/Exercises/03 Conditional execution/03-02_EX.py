#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program
hours=input("Enter Hours: ")
try:
    hrs=float(hours)
except:
    print("Error, please enter numeric input")
    quit()
rate=input("Enter Rate: ")
try:
    rt=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if hrs>40:
    hrs=hrs-40
    pay=(40+hrs*1.5)*rt
else:
    pay=hrs*rt
print("Pay:", pay)
