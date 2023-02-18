import requests
from bs4 import BeautifulSoup

server = "Phoenix"
itemnbr = str(24888)


def scrape(server, itemnumber):

    r = requests.Session()
    r.cookies.update({"mogboard_server": server, "mogboard_last_selected_server": server})
    targeturl = "https://universalis.app/market/" + str(itemnumber)
    c = r.get(targeturl)
    soup = BeautifulSoup(c.content, 'html.parser')

    data_list = []
    history = "NONE"
    listings = True
    history = True

    # ITEM NAME
    itemname = soup.find('div', class_="item_info")
    itemname = itemname.text.split()
    data_list.append(" ".join(itemname[1:]))

    # CURRENT DATA
    data = soup.find('div', class_="tab-page tab-cw open")
    history = data.find('div', class_="cw-history")

    #CHECK FOR LISTINGS
    if 'There are no listings' in data.text:
        listings = False

    #CHECK FOR
    if "Really rare!?" in history.text:
        history = False

    if listings:
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
    else:
        data_list.append('No listings')
        data_list.append('No listings')
        data_list.append('No listings')

    #HISTORY DATA
    if history:
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
    else:
        data_list.append('No history')
        data_list.append('No history')
        data_list.append('No history')
        data_list.append('No history')

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

    # IF NO LISTINGS -> "No listings" x 3
    # IF NO HISTORY -> "No history" x 4

print(scrape("Alpha", itemnbr))

