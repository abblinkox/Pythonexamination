Daniel_Radcliffe = ["man", "brun", "brun", "Daniel Radcliffe"]
Rupert_Grint = ["man", "röd", "blå", "Rupert Grint"]           # vi gör en array för varje kändis egenskaper
Emma_Watson = ["kvinna", "brun", "brun", "Emma Watson"]
Selena_Gomez = ["kvinna", "brun", "brun", "Selena Gomez"]
Linus_Kasper = ["man", "blond", "brun", "Linus Kasper"]
Lindrit_Koxha = ["man", "brun", "brun", "Lindrit Koxha"]
kändisar = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Linus_Kasper, Lindrit_Koxha] # en array med alla kändisar
lookalikes = ""

print("Ange kön:")
kön = str(input())
print("Ange hårfärg:")
hårfärg = str(input())
print("Ange ögonfärg:")   # skapar tre inputs där användaren får svara på frågorna, vi omvandlar svaren på dessa frågor till strings
ögonfärg = str(input())

for personer in kändisar:   #skapar en for loop med tre if satser i
    if personer[0] == kön:      #tittar om inputen matchar könet, hårfärgen, ögonfärgen
        if personer[1] == hårfärg:
            if personer[2] == ögonfärg:     
                lookalikes += personer[3] + ", " #då lägger den till de namn från de arrayerna som inputen matchade, eftersom namnen har plats nummer 3 i arrayerna
if lookalikes == "":   #om inputen ej matchar skriver den ut detta
    print("Du liknar dessvärre ingen kändis...")
else:
    print("Du liknar " + lookalikes + "!") #annars skriver den ut ett meddelande där det står vilka man matchar till