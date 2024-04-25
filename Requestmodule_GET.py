import requests
url = "https://restcountries.com/v3.1/all"
res = requests.get(url)
if res.status_code == 200:
    print("Getting the data")
    data = res.json()
    names = [country["name"]["common"] for country in data]
    for i in names:
        print("The common names of country is:",i)
else:
    print("Request failed")
p_url = "https://httpbin.org/post"
p_data = {'key':'value'}
p_res = requests.post(p_url,data=p_data)

if p_res.status_code == 200:
    print("POST is successful")
else:
    print("POST request fails")

