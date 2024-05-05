import random
score = 0
from random import randint
a = str(input("When was Scratch made? A: 2003 B: 2002 C:2004 D: 1995 "))
if a == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who made tutorials about making Geometry Dash and making tile scrolling platformers on Scratch? A: Gamedeveloper1234 B: Meekaryo C: griffpatch D: The_Updator "))
if a == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("The company that made Among Us? A: Gamefam B: Innersloth C: Roblox D: Hard Games "))
if a == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("9 + 10?? A: 19 B: 21 C: 20 D: 11 + 8 "))
if a == "A" or a == "B" or a == "D":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Is Roblox a kids game? A: Yes B: No C: Maybe D: Depends "))
if a == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who's the general creator of Undertale: A: Toby B: Fox C: Toby Fox D: xoF yobT "))
if a == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("What is Pi: A: An irrational number B: A pie C: 3.14 D: A symbol "))
if a == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Which band made Whistle? A: Imagine Dragons B: Flo Rida C: Josh Hutchson D: Tenacious D "))
if a == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who made Geometry Dash? A: Toby Fox B: Josh Hutchson C: Robtop D: Sat / oru  Go / Jo "))
if a == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("1+1? A: 2 B: 1 C: 5 D: 11 "))
if a == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

print("You have", score * 100000, "dollars over 1000000 dollars")