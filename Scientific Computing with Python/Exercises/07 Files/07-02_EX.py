#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence
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
