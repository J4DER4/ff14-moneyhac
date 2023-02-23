from imports import *

thread_local = threading.local()
item_list = []

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_site, sites)

def download_site(url):
    session = get_session()
    with session.get(url, timeout=5) as response:
        print(url)
        scrape(response, url)
        

def scrape(response, url):

    soup = bs(response.content, "html.parser")

    # Scraping items in europe
    try:
        itemname = " ".join(soup.find('div', class_="item_info").text.split())
        price = soup.find('td', class_="price-current").text.replace(",", "")
        quantity = soup.find('td', class_="price-qty").text.replace(",", "")
        server = soup.find('td', class_="price-server").text

        if server == "Twintania":
            itemname = "Twintania item"
            price = 0
            quantity = 0
            server = "Twintania"
    except:
        pass
    
    # Scraping the median prices of twintania price history
    median_of_price = []

    # I'm bad with beautifulsoup
    twintania_price_history = soup.find('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find_next('div', class_="tab-market-tables").find('div', class_="cw-table cw-history").find('td', class_="price-current")

    next_price = twintania_price_history
    median_of_price.append(int(next_price.text.replace(",", "")))

    for _ in range(9):
        try:
            next_price = next_price.findNext('td', class_="price-current")
            median_of_price.append(int(next_price.text.replace(",", "")))
        except:
            pass
    
    median_of_price = int(stat.median(median_of_price))

    item_list.append([itemname, price, quantity, server, median_of_price, url])