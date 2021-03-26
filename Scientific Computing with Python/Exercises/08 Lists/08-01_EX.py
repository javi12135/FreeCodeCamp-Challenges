#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements

def chop(list):
    list.pop(0)
    list.pop(len(list)-1)
    print(list)

def middle(list):
    return list[1:len(list)-1]

list = [0,1,2,3,4,5,6]
chop(list)

list = [0,1,2,3,4,5,6]
list = middle(list)
print(list)
