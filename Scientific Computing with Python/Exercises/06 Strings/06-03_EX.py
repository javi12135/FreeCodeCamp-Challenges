#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments

#_def count(tocount):
#    count = 0
#    for letter in word:
#        if letter == tocount:
#            count += 1
#    print(count)

word=input("What is your word?: ")
tocount=input("What do you want to count?: ")
print(word.count(tocount))
