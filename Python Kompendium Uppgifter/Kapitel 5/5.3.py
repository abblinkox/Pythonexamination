norden = ["Danmark","Finland","Island","Norge","Sverige"]
storbritannien = ["England", "Nordirland", "Skottland", "Wales"]   #2 arrays med länderna i norden och storbrittanien
print("Ange ett land: ")
land = str(input())  #skapar en input och gör svaret till en string
if land.title() in norden:   #använder oss av .title() metoden för att göra vår string med stor bokstav först, och tittar om inputen matchar någon av länderna
    print(land.title() + " finns i Norden.")
elif land.title() in storbritannien : #om den ej matchar någon av länderna i norden tittar vi i den andra arrayen
    print(land.title() + " ligger i Storbritannien.")
else:
    print(land.title() + " ligger ej i Norden eller Strobritannien.") #om den ej matchar någonstans skriver vi ut detta meddelande
