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
