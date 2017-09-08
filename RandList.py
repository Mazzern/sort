from random import randint
def MakeList():
    li = []
    for i in range(randint(4,20)):
        li.append(randint(0,100))
    return li
