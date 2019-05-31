mängd = range(10000000) #sätter range till 10000000 då vi ska addera så många tal
summa = 0    #sätter summa vid 0
for i in mängd: #adderar alla tal som kommer efter varandra på summan
    summa += i
print(summa)
