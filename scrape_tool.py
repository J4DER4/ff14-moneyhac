import requests
from bs4 import BeautifulSoup

server = "Phoenix"
itemnbr = str(24888)
targeturl = "https://universalis.app/market/" + itemnbr

def scrape(server, itemnumber):

    r = requests.Session()
    r.cookies.update({"mogboard_server": server, "mogboard_last_selected_server": server})
    c = r.get(targeturl)
    soup = BeautifulSoup(c.content, 'html.parser')

    data_list = []
    history = "NONE"

    # ITEM NAME
    itemname = soup.find('div', class_="item_info")
    data_list.append(soup.find('div', class_="item_info").text)

    # CURRENT DATA
    data = soup.find('div', class_="tab-page tab-cw open")
    print(data)

    #CHECK FOR LISTINGS
    if 'There are no listings' in data:
        print("NO Listings")

    for entry in data:
                # Price_sinle
        if (entry.find("td", class_="price-current")):
            data_list.append(entry.find("td", class_="price-current").text)
                # quanity
        if (entry.find("td", class_="price-qty")):
            data_list.append(entry.find("td", class_="price-qty").text)
                # total price
        if (entry.find("td", class_="price-total")):
            data_list.append((entry.find("td", class_="price-total")).text)
                    # History
        if (entry.find('div', class_="cw-table cw-history")):
            history = entry.find('div', class_="cw-history")

    #HISTORY DATA

    for entry in history:
        # Price_sinle
        if (entry.find("td", class_="price-current")):
            data_list.append(entry.find("td", class_="price-current").text)
        # quanity
        if (entry.find("td", class_="price-qty")):
            data_list.append(entry.find("td", class_="price-qty").text)
        # total price
        if (entry.find("td", class_="price-total")):
            data_list.append((entry.find("td", class_="price-total")).text)
        if (entry.find("td", class_="price-date")):
            data_list.append((entry.find("td", class_="price-date")).text)
    return data_list


    #PACKAGING

    # 1 ITEM NAME
    # 2 PRICE SINGLE
    # 3 QUANITY
    # 4 PRICE TOTAL
    # 5 H PRICE SINGLE
    # 6 H QTY
    # 7 H TOTAL
    # 8 LAST SOLD
print(scrape("Shiva", itemnbr))

