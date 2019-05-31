registrerade =["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar =["Anna", "Erik", "Karl"]

for namn in avanmälningar:
    del registrerade[registrerade.index(namn)] #för varje namn i avanmälnigar tar den bort samma namn från registrerande.
    
print (registrerade)