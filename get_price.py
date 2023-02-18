import requests as rq
from bs4 import BeautifulSoup as bs

SERVER_LIST = ["Alpha", "Lich", "Odin", "Phoenix", "Raiden", "Shiva", "Zodiark"]

def url_gen():
    return [f"https://universalis.app/market/{i}" for i in range(40000)]




def main():

    item_list = []

    url_list = url_gen()
    session = rq.Session()

    for url in url_list:
        try:
            for server in SERVER_LIST:
                
                session.cookies.update({"mogboard_server" : server, "mogboard_last_selected_server": server})

                open_url = session.get(url)
                soup = bs(open_url.content, 'html.parser')

                item_name = soup.find('div', class_="item_info")
                item_price = soup.find('div', class_="tab-page tab-cw open")

                if url == "https://universalis.app/market/24888":
                    print(url)

                for entry in item_price:
                    if(entry.find("td", class_="price-current")):
                        price = entry.find("td", class_="price-current")
                        item_list.append(item_name.text)

                

        except:
            pass
    print(item_list)
main()