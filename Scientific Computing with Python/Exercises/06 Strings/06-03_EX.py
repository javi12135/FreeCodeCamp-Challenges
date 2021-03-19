#_def count(tocount):
#    count = 0
#    for letter in word:
#        if letter == tocount:
#            count += 1
#    print(count)

word=input("What is your word?: ")
tocount=input("What do you want to count?: ")
print(word.count(tocount))
