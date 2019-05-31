import web, ui, random #importerar allt vi behöver

integer = 1
correctAnsNum = 0
correctAns = 0
count = 0
numbers = list(range(25)) #Vi gör en array med nummer från 0-24
random.shuffle(numbers) #blandar om siffrorna i arrayen
easyAPI = web.get("https://opentdb.com/api.php?amount=25&category=18&difficulty=easy&type=multiple")["results"] #api med lätta frågor
hardAPI = web.get("https://opentdb.com/api.php?amount=25&category=18&difficulty=medium&type=multiple")["results"] #api med svåra frågor
QA = [] #en tom array där vi kommer att lägga in frågor,svar och rätt svar


def NumbersGet(): #funktion för att hämta ett index som är blir random och som bara returnas en gång
    global index #gör en global variabel så den kan användas utanför funktionen också
    index = numbers[0] #index blir första värdet
    del numbers[0] #tar bort första värdet i listan
    return index 

def AltGet(index): #funktion för att blanda alternativen i random ordning
    global alt
    alt = [] 
    alt.append(QA[index]["correct"]) #lägger till rätta svaret i tomma arrayen
    for i in QA[index]["incorrect"]: 
        alt.append(i) #lägger till felaktiga svaren i arrayen
    random.shuffle(alt) #blandar om värdena
    return alt #returnerar arrayen

def APIget(api): #funktion som lägger in värden i QA arrayen
    for i in api:    #en dictionary läggs in för varje plats i arrayen med fråga och svar och rätt svar
        QA.append({"fråga" : i["question"], "correct" : i["correct_answer"], "incorrect" : i["incorrect_answers"]})


def ValNum(x, num): #funktion för att kolla om det man skickar in är ett nummer mellan vissa värden
    if (x != 0):
        try:
            float(x) #om det inte går att göra till en float är det en string, då returnas false
            if (int(x)!= 0): #nummret får inte vara 0
                if(int(x) < num): #nummret får inte vara högre än num                
                    return True
            return False
        except ValueError:
            return False
    else:
        return False


def whatDiff(): #funktion för svårighetsgrad
    ui.header("Difficulty")
    ui.echo("1: Easy")
    ui.echo("2: Hard")
    difficulty = ui.prompt("Answer >")
    if difficulty == "1": 
        APIget(easyAPI) #svar 1 ger lättare frågor
    elif difficulty == "2":
        APIget(hardAPI) #svar 2 ger svåra frågor
    else:
        ui.echo("Invalid input, try again")
        ui.line()
        whatDiff() #om något annat än 1 eller 2 anges så körs den om

def outpttxt(header, echo):
    ui.header(header)
    ui.echo(echo)
    ui.line()


def numbQ():
    global questions 
    ui.echo("Number of questions, 1 - 25")
    questions = ui.prompt("Answer >")
    if ValNum(questions, 26): #om nummret ligger mellan 1-25 returneras true 
        return questions  #skickar tillbaka antalet frågor som ska finnas
    else:
        ui.echo("Invalid input, try again")
        ui.line()
        numbQ() #funktionen körs om ogiltigt svar kommer in

def replace(str): #tar bort onödiga tecken 
    str = str.replace("&lt;", "<")
    str = str.replace("&gt;", ">")
    str = str.replace("&quot;", '"')
    str = str.replace("&#039;", "'")
    #vi uppdaterar str för varje rad med de riktiga teckena
    return str 

ui.line()
ui.header("Frågesport")
ui.line()
whatDiff()
ui.line()
ui.header("Questions")
numbQ()
ui.line()
while True: #frågesporten körs tills antalet frågor har uppnåtts, då stoppas den
    if count != int(questions): 
        count += 1 #antalet gånger programmet har ställt en fråga, lägger till 1 när en ny fråga ställs
        NumbersGet()
        ui.echo(replace(QA[index]["fråga"])) #frågan
        ui.echo("Alternatives:")
        AltGet(index) #hämtar alternativ
        for i in alt:
            if i == QA[index]["correct"]: #om rätt svar
                correctAnsNum = integer #sparar det rätta värdets plats
            ui.echo(replace(str(integer) + ": " + i)) #skriver ut alternativen
            integer += 1
        svar = ui.prompt("Answer >")
        if ValNum(svar, 5): #om svaret är mellan 1 och 4
            if alt[int(svar)-1] == alt[correctAnsNum -1]: #om svaret är korrekt
                correctAns += 1 #lägger till ett poäng i minne 
                outpttxt("Your score: " + str(correctAns), "Correct! Your answer was " + str(correctAnsNum)) #anropar outpttxt som sätter fel/rätt
                integer = 1
            else:
                outpttxt("Your score: " + str(correctAns), "Wrong! Correct answer was " + str(correctAnsNum)) 
                integer = 1
        else:
            outpttxt("Your score: " + str(correctAns), "Correct! Your answer was " + str(correctAnsNum)) 
            integer = 1
    else: #om programmet frågat lika många frågor som användaren har valt
        ui.line()
        ui.header("Your final score: " + str(correctAns) + "/" + questions) #skriver ut en slutgiltig poäng
        ui.header("Thank you for playing!")
        ui.line()
        break 
