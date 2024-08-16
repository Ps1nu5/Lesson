import requests
from bs4 import BeautifulSoup

url = 'https://www.codewars.com/users/Ps1nus'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

account_creation_date = soup.findAll('div', class_='stat')

for i in account_creation_date:
    i = i.text
    if 'Since' in i:
        date = i[13:]
        print(date)




