import requests 



response=requests.get('https://api.kanye.rest/')

if response.status_code == 200:
    quote = response.json()
    print(quote['quote'])