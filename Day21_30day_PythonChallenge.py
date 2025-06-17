#make sure you install both the libraries requests and bs4 first

import requests
from bs4 import BeautifulSoup 

url = "https://www.ndtv.com/" #news website

response = requests.get(url) #storing data from website in variable

if response.status_code == 200: #confirming if response is correct using status code 200
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')
    
    print("Latest Headlines:") #output
    for idx, headline in enumerate(headlines, 1):
        print(f"{idx}. {headline.get_text(strip=True)}")
else:
    print(f"Failed!! Status code: {response.status_code}") #failure message