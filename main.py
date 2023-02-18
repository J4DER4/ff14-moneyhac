import requests
from bs4 import BeautifulSoup


server = "Phoenix"
r = requests.Session()
r.cookies.update({"mogboard_server" : server, "mogboard_last_selected_server": server})
c = r.get("https://universalis.app/market/24888")

#print(r)
soup = BeautifulSoup(c.content, 'html.parser')
#print(soup.title)


# ITEM NAME
itemname = soup.find('div', class_="item_info")
print(itemname.text)

#Price

itemprice = soup.find('div', class_="tab-page tab-cw open")
#price = soup.itemprice.find_all("td", class_="price-current")

for entry in itemprice:
   if(entry.find("td", class_="price-current")):
       price = entry.find("td", class_="price-current")
#price = lines = itemprice.find_all("price-current")
#print(itemprice.text)
print(price.text)

