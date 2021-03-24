ask = True
count = 0
while ask == True:
    filename = input("Enter a file name: ")
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
    else:
        try:
            filehandle = open(filename)
            ask = False
        except:
            continue
for line in filehandle:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", filename)
