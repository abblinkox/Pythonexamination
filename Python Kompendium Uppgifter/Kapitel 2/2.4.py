print("Hallå!") 
print("Hur gammal är du?") 
ålder= int(input()) 
årtillmyndig = 18-ålder #skapar en variabel som visar om hur många år man blir myndig
årmyndig = ålder-18 #skapar en variabel som visar hur många år man har varit myndig
if ålder < 18:
    print("Du är myndig inom "+ str(årtillmyndig) + " år!") #om ålder är mindre än 18 så skrivs detta meddelande
elif ålder > 18:
    print("Du har varit myndig i " + str(årmyndig)+ " år!") #är den över 18 skrivs detta meddelande
elif ålder == 18:
    print("Du har precis blivit myndig!") #är ålder 18 skrivs detta meddelande
    