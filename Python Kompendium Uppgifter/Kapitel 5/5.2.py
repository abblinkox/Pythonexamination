sömnbehov = ["14","13","12","11.5","11","11","10,5","10","10","10","9.5","9","9","9","9","8.5","8"] #vi gör en array där vi skriver in alla åldrars sömnbehov
print("Ange ditt namn: ")
namn= str(input())
print("Ange ditt ålder: ")
ålder= int(input())
if ålder > 17: #om ålder är större än 17 ska den alltid skriva ut att användaren behöver 8 timmars sömn
    print("Hallå " + namn.title() + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(ålder) + " år) sova minst 8 timmar per natt.")
else: #annars ska den skriva ut det objekt som står i plats (ålder-1) i arrayen, tex om man skriver in 1 så kommer den att välja objektet i plats 0, dvs 14 timmar.
    print("Hallå " + namn.title() + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(ålder) + " år) sova minst " + str(sömnbehov[ålder-1]) + " timmar per natt.")