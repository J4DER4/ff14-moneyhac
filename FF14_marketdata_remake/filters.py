from data_scraper import item_list

def filter_twintania_cheaper(filtered_list):
    for item in item_list:
        try:
            if int(item[1]) > int(item[4]):
                filtered_list.remove(item)
        except:
            pass

def filter_price_higher_than_cash(cash, filtered_list):
    for item in item_list:
        try:
            if int(item[1]) * int(item[2]) > cash:
                filtered_list.remove(item)
        except:
            pass

def filter_under_margin_trades(filtered_list):
    for item in item_list:
        try:
            if ((int(item[4]) - int(item[1])) * int(item[2])) < 50000:
                filtered_list.remove(item)
        except:
            pass

def filter_twintania_item(filtered_list):
    for item in item_list:
        try:
            if int(item[1]) == 0:
                filtered_list.remove(item)
        except:
            pass

def filter():

    filtered_list = item_list[:]

    cash = 100000
    try:
        cash = int(input("Enter the amount of cash at hand (Default 100K):\n"))
    except:
        pass
    if cash == "":
        cash = 100000

    print("Filtering out bad trades...\n")
    
    filter_twintania_cheaper(filtered_list)
    filter_price_higher_than_cash(cash, filtered_list)
    filter_under_margin_trades(filtered_list)
    filter_twintania_item(filtered_list)
    
    return filtered_list