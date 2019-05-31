multitab = int(input("Ange en multiplikationstabell: "))  #en vanlig input där man skriver in sin tabell
number = 0   #två variabler vi använder sedan
check = 0
while True:
    print(multitab*number)   #skriver ut inputen gånger nummer
    number += 1       #lägger +1 varje gång loopen körs
    check += 1
    if check == 3:  #när check sedan når 3 pausar vi och nollställer check
        check = 0
        answer = str(input("Fortsätt? "))   #vi frågar om man vill fortsätta
        if answer.lower() == "ja":  #om svaret är ja fortsätter vi, annars avslutar vi
            continue
        else:
            break