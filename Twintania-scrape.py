import requests
from bs4 import BeautifulSoup


server = "Shiva"
itemnbr = str(24888)
targeturl = "https://universalis.app/market/" + itemnbr


r = requests.Session()
r.cookies.update({"mogboard_server" : server, "mogboard_last_selected_server": server})
c = r.get(targeturl)

#print(r)
soup = BeautifulSoup(c.content, 'html.parser')
print(soup.title)

# ITEM NAME
itemname = soup.find('div', class_="item_info")

# CURRENT DATA
data = soup.find('div', class_="tab-page tab-cw open")

#price = soup.itemprice.find_all("td", class_="price-current")

qty = "NONE"
price_single = "NONE"
price_total = "NONE"

for entry in data:
    #Price_sinle
    if(entry.find("td", class_="price-current")):
        price_single = entry.find("td", class_="price-current")
    #quanity
    if(entry.find("td", class_="price-qty")):
        qty = entry.find("td", class_="price-qty")
    #total price
    if(entry.find("td", class_="price-total")):
        price_total = (entry.find("td", class_="price-total"))
        #History
    if(entry.find('div', class_="cw-table cw-history")):
        history = entry.find('div', class_="cw-history")
    if (entry.find("td", class_="price-date")):
        h_date = (entry.find("td", class_="price-date"))

#History

h_qty = "NONE"
h_price_single = "NONE"
h_price_total = "NONE"

for entry in history:
    #Price_sinle
    if(entry.find("td", class_="price-current")):
        h_price_single = entry.find("td", class_="price-current")
    #quanity
    if(entry.find("td", class_="price-qty")):
        h_qty = entry.find("td", class_="price-qty")
    #total price
    if(entry.find("td", class_="price-total")):
        h_price_total = (entry.find("td", class_="price-total"))








# OUTPUT
nqqty = 3
nqprice = "1,000"
print((float(nqqty)*float(nqprice.replace(",", ""))))