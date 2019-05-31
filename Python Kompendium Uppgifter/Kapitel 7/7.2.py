import random   #importerar random

randomnummer = random.randint(0,99)   #får random siffror med hjälp av random

print("Write a number!")
nummer = int(input())
guesses = 0
while nummer != randomnummer:  # när nummer inte är lika med randomnummer
    guesses +=1   #vi lägger till en på guesses
    if nummer < randomnummer:   #om nummret är högre än randomnummer, skriv ut "HIGHER" och "Write a new number!""
        print("HIGHER")
        print("Write a new number!")
        nummer = int(input())
    else:
        print("LOWER")     # annars gör vi motsatsen
        print("Write a new number")
        nummer = int(input())

print("Congratulations, you have found the right number! It only took you " + str(guesses) + " guesses!") #när man får samma nummer avbryts while loopen och detta skrivs ut