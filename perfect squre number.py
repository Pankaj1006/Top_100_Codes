import math


def checkperfectsquare(x):
    if (math.ceil(math.sqrt(n)) ==
            math.floor(math.sqrt(n))):
        print("True")
    else:
        print("False")

n = int(input("Enter a number:: "))
checkperfectsquare(n)
