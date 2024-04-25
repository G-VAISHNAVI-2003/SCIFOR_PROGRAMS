import requests
url = "https://restcountries.com/v3.1/all"
res = requests.get(url)
if res.status_code == 200:
    print("Everything is fine")
else:
    print("An error ")
data = res.json()
off = [country["name"]["official"] for country in data]
names = [country["name"]["common"] for country in data]
for j in off:
    print("The official of country is:",j)
for i in names:
    print("The common names of country is:",i)
