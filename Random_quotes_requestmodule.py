import requests
def quote():
    url = "https://api.quotable.io/random"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data['content'],data['author']
    else:
        return "Fetching failed"
qu,au = quote()
print("THE RANDOM QUOTE IS :\n",qu)
print("THE AUTHOR IS:",au)


