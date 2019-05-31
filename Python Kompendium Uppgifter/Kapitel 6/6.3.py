import requests    
print("---ARTIST DB---")

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" 

r = requests.get(url)
APIresponse = r.json()                 
artists = APIresponse["artists"]

for i in artists:
    print(i["name"])    
print("-------------")
print("Select artist:")
name = str(input())
print("-------------")

names = ["Ariana Grande", "Avicii", "Blink-182", "Brad Paisley", "Ed Sheeran", "Imagine Dragons", "Maroon 5", "Scorpions"]

if name.title() in names:     
    for i in artists:
        if i["name"] == name.title():       
            artistid = i["id"]
            url2 = url + str(artistid)
            r = requests.get(url2)
            APIresponse = r.json()
            genres = APIresponse["artist"]["genres"]
            members = APIresponse["artist"]["members"]
            print(APIresponse["artist"]["name"])
            print("*************")
            print("Genres: ")
            for i in genres:
                print(i)
            print("Years active: " + APIresponse["artist"]["years_active"][0])
            print("Members: ")
            for i in members:
                print(i)
            print("-------------")
else:
    print("Invalid input")  
