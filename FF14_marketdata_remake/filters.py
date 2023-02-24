from data_scraper import item_list

def filter_twintania_cheaper():
    for item in item_list:
        if int(item[1]) > int(item[4]):
            item_list.remove(item)

def filter_price_higher_than_cash(cash):
    for item in item_list:
        if int(item[1]) * int(item[2]) > int(item[4]) * int(item[2]):
            item_list.remove(item)

def filter_under_margin_trades():
    for item in item_list:
        if int(item[4]) * int(item[2]) - int(item[1]) * int(item[2]) < 50000:
            item_list.remove(item)

def filter_twintania_item():
    for item in item_list:
        if int(item[1]) == 0:
            item_list.remove(item)

def filter():

    cash = 100000
    try:
        cash = int(input("Enter the amount of cash at hand (Default 100K):\n"))
    except:
        pass
    if cash == "":
        cash = 100000

    print("Filtering out bad trades...\n")
    
    filter_twintania_cheaper()
    filter_price_higher_than_cash(cash)
    filter_under_margin_trades()
    filter_twintania_item()
    