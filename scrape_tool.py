import requests
from bs4 import BeautifulSoup
import time
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
    try:
        #NO MARKET DATA CHECK
        if data.find(class_="item-no-data"):
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
            data_list.append("NO DATA")
        else:
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

            #EUROPE

            #HIGH QUALITY
            hqqty = "NONE"
            hqprice = "NONE"
            hqserver = "NONE"

            hq = soup.select_one('div.cheapest:-soup-contains("Cheapest HQ")')
            hq = hq.find("div", class_="cheapest_price")
            try:
                if hq.find(class_="cheapest_value"):
                    #HQ PRICE
                    hqprice = hq.find(class_="cheapest_value").text.strip()
                    data_list.append(hqprice)

                    # HQ QTY
                    hqqty = hq.find("em").text.split()[0]
                    data_list.append(hqqty)

                    # HQ TOTAL
                    data_list.append(float(hqqty).replace(",", "") * float(hqprice).replace(",", ""))

                    #HQ SERVER
                    hqserver = hq.find(class_="cheapest_price_info").text.split()[1]
                    data_list.append(hqserver)



            except AttributeError:
                #NO HQ VARIANT OR OUT OF STOCK
                data_list.append("NO HQ")
                data_list.append("NO HQ")
                data_list.append("NO HQ")
                data_list.append("NO HQ")

            #NQ QTY
            nqqty = "NONE"
            nqprice = "NONE"
            nqserver = "NONE"



            nq = soup.select_one('div.cheapest:-soup-contains("Cheapest HQ")+ .cheapest')
            nq = nq.find("div", class_="cheapest_price")

            try:
                if nq.find(class_="cheapest_value"):
                    #NQ PRICE
                    nqprice = nq.find(class_="cheapest_value").text.strip()
                    data_list.append(nqprice)

                    # NQ QTY
                    nqqty = nq.find("em").text.split()[0]
                    data_list.append(nqqty)

                    #NQ TOTAL
                    data_list.append(float(nqqty.replace(",", ""))*float(nqprice.replace(",", "")))


                    #NQ SERVER
                    nqserver = nq.find(class_="cheapest_price_info").text.split()[1]
                    data_list.append(nqserver)


            except AttributeError:
                # NO NQ VARIANT OR NO OUT OF STOCK
                data_list.append("NO HQ")
                data_list.append("NO HQ")
                data_list.append("NO HQ")
                data_list.append("NO HQ")
    except AttributeError:
        pass


    return data_list


    #PACKAGING
#TWINTANIA
    # 1 ITEM NAME
    # 2 PRICE SINGLE
    # 3 QUANITY
    # 4 PRICE TOTAL
#TWINTANIA HISTORY
    # 5 H PRICE SINGLE
    # 6 H QTY
    # 7 H TOTAL
    # 8 H LAST SOLD
#EU HQ & LQ
    # 9 HQ PRICE
    # 10 HQ QTY
    # 11 HQ TOTAL
    # 12 HQ SERVER
    # 13 NQ PRICE
    # 14 NQ QTY
    # 15 NQ TOTAL
    # 16 NQ SERVER

    # IF NO LISTINGS -> "No listings" x 3
    # IF NO HISTORY -> "No history" x 4
    # IF NO HQ -> "NO HQ" x 4
# IF NO NQ -> "NO NQ" x 4


print(scrape("Twintania", "5163"))