numberinput=None
total=0
count=0
while True:
    numberinput=input("Enter a number: ")
    if numberinput=="done":
        break
    else:
        try:
            numberinput = float(numberinput)
            total=total+numberinput
            count=count+1
        except:
            print("Invalid input")
average=total/count
print(total,count,average)
