import string
from random import random, randint


def random_user_id ():
    
    chars = string.ascii_letters

    myCode = ''
    for i in range(6):
        myChar = chars[randint(0,50)]
        myDigit = randint(0,9)
        if(i%2==0):
            myCode = str(myCode)  + str(myChar)
        else:
            myCode = str(myCode)  + str(myDigit)
    
    return myCode

