def header(message):   #vi gör funktionen header
    messlängd= len(message)   #använder oss av len funktionen för att bestämma hur lång meddelandet är
    mellanrum= (30-messlängd)/2  # mellanrumen på sidorna ska vara 30 - längden då vi max kan ha 30 i längd
    output = ""
    for i in range(31):
        if i == 0:     #här skriver den ut ett "|" på första objektet
            output += "|"
        if mellanrum > i > 0:  #därefter skriver den ut mellanrum tills den kommer till själva texten
            output += " "
        if i == mellanrum:         # när i == mellanrum skriver den ut meddelandet
            output += message                                                                        
        if 30 > i > mellanrum + messlängd:   #därefter skriver den ut mer mellanrum
            output += " "
        if i == 30:
            output += "|" #och avslutar med en till "|"
    
    print(output)

def line (boolean = False):   #sålänge vi skriver i funktionen att den ska vara FALSE skriver den ut många "*", om vi skriver att den är true skriver den istället många "-"
    if boolean == True:
        print("---------------------------------")
    else:
        print("**********************************")

def echo (string):   #skriver ut en vanlig string med "|" framför
    print("| " + string)

def prompt (string):  #ett input
    return input("| " + string)

