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
