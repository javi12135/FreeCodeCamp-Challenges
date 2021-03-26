#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case
ask = True
while ask == True:
    filename = input("Enter a file name: ")
    try:
        filehandle = open(filename)
        ask = False
    except:
        continue
filecontent = filehandle.read()
filecontent = filecontent.upper()
print(filecontent)
