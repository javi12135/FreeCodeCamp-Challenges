#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average
numberinput=None
largest=None
smallest=None
while True:
    numberinput=input("Enter a number: ")
    if numberinput=="done":
        break
    else:
        try:
            numberinput=float(numberinput)
        except:
            print("Invalid input")
            continue
        if largest==None:
            largest=numberinput
            smallest=numberinput
        elif numberinput>largest:
            largest=numberinput
        elif numberinput<smallest:
            smallest=numberinput
print("Maximum is",largest)
print("Minimum is",smallest)
