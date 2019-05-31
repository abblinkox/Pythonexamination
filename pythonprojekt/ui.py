def header(message):
    messlängd= len(message)
    mellanrum= (30-messlängd)/2
    output = ""
    for i in range(31):
        if i == 0:
            output += "|"
        if mellanrum > i > 0:
            output += " "
        if i == mellanrum:
            output += message                                                                        
        if 30 > i > mellanrum + messlängd:
            output += " "
        if i == 30:
            output += "|"
    
    print(output)

def line (boolean = False):
    if boolean == True:
        print("---------------------------------")
    else:
        print("**********************************")

def echo (string):
    print("| " + string)

def prompt (string):
    return input("| " + string)

