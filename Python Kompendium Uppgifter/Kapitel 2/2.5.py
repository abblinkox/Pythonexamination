import math

print("Hur många vill äta 2 vanliga korvar?")
korvar2= int(input())
print("Hur många vill äta 3 vanliga korvar?")
korvar3= int(input())
print("Hur många vill äta 2 veganska korvar?")
vkorvar2= int(input())
print("Hur många vill äta 2 veganska korvar?")
vkorvar3= int(input())

antvanförpack = (korvar2 * 2 + korvar3 * 3)/8 
print("Det behövs "+ str(math.ceil(antvanförpack)) + " vanliga korvar") #använder math.ceil för att avrunda alla tal uppåt.
antvegförpack = (vkorvar2 * 2 + vkorvar3 * 3)/4 
print("Det behövs "+ str(math.ceil(antvegförpack))+ " veganska korvar")
antläsk = korvar2 + korvar3 + vkorvar2 + vkorvar3
print("Det behövs "+ str(antläsk)+ " drickor!" ) 

kostvan = antvanförpack * 20.95
kostveg = antvegförpack * 34.95
kostläsk = antläsk * 13.95
totkost = kostvan + kostveg + kostläsk #skapar variabler och lägger ihop dem för den totala kostnaden
print("Utflykten kostar totalt "+ str(math.ceil(totkost))+ " kr.")