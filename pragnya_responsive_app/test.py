import requests 




class Quotes:
    def __init__(self) -> None:
        self.response = requests.get('https://api.kanye.rest/')
        
        if self.response.status_code == 200:
            self.quote = self.response.json()['quote']
            print(self.quote)  # Print the quote
        else:
            self.quote = None  # Handle the case when the API call fails
            print("Failed to retrieve quote.")

# Create an instance of the Quotes class
# quotes = Quotes()


