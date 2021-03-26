#Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist
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
