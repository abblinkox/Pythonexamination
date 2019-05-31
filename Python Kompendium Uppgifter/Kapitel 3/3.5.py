male = [
    "Erik",
    "Lars",
    "Karl",
    "Anders",
    "Johan"
]

female = [
    "Maria",
    "Anna",
    "Margareta",
    "Elisabeth",
    "Eva"
]

print("Vilket namn ska tas bort?")
namn = str(input())
if namn in male:           # tittar om namnet är i arrayen male, då tar den bort den därifrån
    male.remove(namn)
    print("Män: ", male )
    print("Kvinnor: ", female )
elif namn in female:       # om namnet inte finns i male, tittar den om namnet finns i female
    female.remove(namn)
    print("Män: ", male )
    print("Kvinnor: ", female )
else:
    print("Namnet finns ej med på någon av listorna")   # om namnet inte finns i någon av arrayerna skriver den ut detta meddelande

