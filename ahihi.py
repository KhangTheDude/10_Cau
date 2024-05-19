import random
score = 0
import time
import datetime

# Create class that acts as a countdown
def countdown(h, m, s):

    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:

        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
       
        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

    print("Bzzzt! The countdown is at zero seconds!")

# Inputs for hours, minutes, seconds on timer
h = 0
m = 0
s = 10
print("When was Scratch made? A: 2003 B: 2002 C:2004 D: 1995 ")
countdown(h, m, s)
a = str(input(""))
if a.upper()== "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who made tutorials about making Geometry Dash and making tile scrolling platformers on Scratch? A: Gamedeveloper1234 B: Meekaryo C: griffpatch D: The_Updator "))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("The company that made Among Us? A: Gamefam B: Innersloth C: Roblox D: Hard Games "))
if a.upper() == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("9 + 10?? A: 19 B: 21 C: 20 D: 11 + 8 "))
if a.upper() == "A" or a.upper() == "B" or a.upper() == "D":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Is Roblox a kids game? A: Yes B: No C: Maybe D: Depends "))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who's the general creator of Undertale: A: Toby B: Fox C: Toby Fox D: xoF yobT "))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("What is Pi: A: An irrational number B: A pie C: 3.14 D: A symbol "))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Which band made Whistle? A: Imagine Dragons B: Flo Rida C: Josh Hutchson D: Tenacious D "))
if a.upper() == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who made Geometry Dash? A: Toby Fox B: Josh Hutchson C: Robtop D: Sat / oru  Go / Jo "))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("1+1? A: 2 B: 1 C: 5 D: 11 "))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Which company made Pizza Tower: A: Tour De Pizza B: Mc Pig C: Pizza Tower Guy D: Hard Games "))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who made Fur Elise: A: Hitler B: Mozart C: Beethoven D: Stalin"))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("ILL MAKE, __ __ : A: YOU GAY B: YOU SAY C: HIM GAY D: HIM SAY"))
if a.upper() == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("6 + 9:  A: 69 B: 96 C: -3 D: 15"))
if a.upper() == "D":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Who are you: A: yourself B: A bot C: A human D: A player "))
if a.upper() == "A" or a.upper() == "C" or a.upper() == "D":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("What level in Pizza Tower revolves around being a cheese hybrid monster: A: Peppibot B: Oh Crap! C: Oh Shit! D: Holy Cow! "))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("Say an artist's name: A: Hitler B: Elise C: Jenny D: Spider-Man"))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("When was Roblox publically released: A: 1999 B: 2006 C: 2005 D: 2007"))
if a.upper() == "B":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("A popular hacker in Among Us: A: No Visor B: 666 C: sire sorol D: Murr3y"))
if a.upper() == "C":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1

a = str(input("2+3: A: 5 B: 6 C: 7 D: 4"))
if a.upper() == "A":
    print("correct")
    score = score + 1
else:
    print("wrong")
    score = score - 1


print("You have", score * 50000, "dollars over 1000000 dollars")
