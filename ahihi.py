import random
score = 0
from random import randint
for i in range(0,10):
    a = random.randint(1.0,10.0)

    b = random.randint(1.0,10.0)

    d = random.randint(1,1)
    if d == 1:
        c = "/"
        ans = a/b
    elif d == 2:
        c = "+"
        ans = a+b
    elif d == 3:
        c = "-"
        ans = a-b
    else:
        c = "*"
        ans = a * b
    ques = float(input("What's " + str(a)+ c + str(b) +" ? "))
    if ques == ans:
        score = score + 1

print("You've got ", ques, " out of 10")