import requests 
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
print(doc)

# response = requests.get('https://www.zara.com/us/en/woman-outerwear-l1184.html?v1=2185970&regionGroupId=1')

# soup = BeautifulSoup(response.text, 'html.parser')

# product_divs = soup.find_all('div' , class_='product')

# for div in product_divs:
#     name = div.find('span', class_='name').text
#     price = div.find('span', class_='price').text
#     print(name, price)
