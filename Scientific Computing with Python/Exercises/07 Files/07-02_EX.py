ask = True
number = 0
count = 0
while ask == True:
    filename = input("Enter a file name: ")
    try:
        filehandle = open(filename)
        ask = False
    except:
        continue
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count += 1
    number += float(line[20:])
print("Average spam confidence:",number/count)
