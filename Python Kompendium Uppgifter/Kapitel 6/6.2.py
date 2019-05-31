import requests   #importerar biblioteket som behövs

print("Enter the cities name")
city = str(input()) #ett vanligt input

cities = [
    "stockholm",   #en vanlig array med städerna
    "uppsala",
]

if city.lower() in cities:
    url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower()  #om staden finns med i arrayen, gör en request till APIn med den staden
    r = requests.get(url)
    APIresponse = r.json()
    forecasts = APIresponse["forecasts"]     
    print("Forecasts: ")
    print(forecasts[0]["date"] + " is prognosed to be " + forecasts[0]["forecast"] )
    for i in forecasts:  # går igenom varje datum och skriver ut deras värden
        print(i["date"] + " is prognosed to be " + i["forecast"])
else:
    print("Invalid city")
