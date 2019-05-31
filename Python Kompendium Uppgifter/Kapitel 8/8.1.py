nummer = input("Vad vill du omvandla? >")

def km_to_miles(km):
    return str(km * 0.621371192) #gör 2 funktioner som omvandlar från km till miles och miles till km

def miles_to_km(miles):
    return str(miles / 0.621371192)



if "km" in nummer:
    print(km_to_miles(int(nummer[0:len(nummer)-2])) + " miles.") #Vi slicar bort enheten från stringen så vi bara får själva talet, och då gör vi talet till en int och lägger in den i funktionen och sedan skriver ut det.

elif "miles" in nummer:
    print(miles_to_km(int(nummer[0:len(nummer)-5])) + " km.")
