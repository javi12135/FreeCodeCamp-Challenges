def computepay(hrs,rt):
    if hrs>40:
        hrs=hrs-40
        pay=(40+hrs*1.5)*rt
    else:
        pay=hrs*rt
    return pay

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
p = computepay(hrs,rt)
print("Pay:", p)
