summa = 0
mängd = range(500)
for i in mängd:
    if i%2 !=0:  # delar talet med 2 och tittar om det kommer rest, finns det rest så adderar den talet då det är ett udda tal
        summa += i
print(summa)