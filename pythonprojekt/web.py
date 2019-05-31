import requests      #importerar biblioteket requests
def get(url): #en funktion som ska ge ut svaret i apiet för respektive url man har som argument
     r = requests.get(url)
     return r.json() #returnerar svaret