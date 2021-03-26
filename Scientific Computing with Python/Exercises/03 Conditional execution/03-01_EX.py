#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
hours=input("Enter Hours: ")
hrs=float(hours)
rate=input("Enter Rate: ")
rt=float(rate)
if hrs>40:
    hrs=hrs-40
    pay=(40+hrs*1.5)*rt
else:
    pay=hrs*rt
print("Pay:", pay)
