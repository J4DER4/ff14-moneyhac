from imports import *
from data_scraper import *


def filter(trade_margin):

    print("Filtering out bad trades...\n")

    index_list = []
    filtered_list = item_list[:]
    for item_index in range(0, len(item_list)):

        # if price is higher on twintania delete the item
        if int(item_list[item_index][1]) > int(item_list[item_index][4]):
            index_list.append(item_list[item_index])
    
    for removal in index_list:
        filtered_list.remove(removal)
    index_list.clear()
        
    
    filtered_list2 = filtered_list[:]
    for item_index in range(0, len(filtered_list)):

        # if price is sold is more than five times smaller it's probably a bait
        if int(filtered_list[item_index][1]) * 5 < int(filtered_list[item_index][4]):
            index_list.append(filtered_list[item_index])
            
    for removal in index_list:
        filtered_list2.remove(removal)
    index_list.clear()
    
    filtered_list3 = filtered_list2[:]
    for item_index in range(0, len(filtered_list2)):

        # if the profit is under {margin} delete the item
        item_difference = (int(filtered_list2[item_index][4]) - int(filtered_list2[item_index][1])) * int(filtered_list2[item_index][2])
        if item_difference < trade_margin:
                index_list.append(filtered_list2[item_index])

    for removal in index_list:
        filtered_list3.remove(removal)            

    return filtered_list3

def main():

    start_index = 0
    end_index = 14014

    with open("FF14_marketdata_remake/item_urls.txt", "r") as file:
        all_sites = [line.rstrip() for line in file]
    
    try:
        end_index_temp = int(input("Input the end index (1 - 14014)\n"))
        if 1 <= end_index_temp <= 14014 and end_index_temp > start_index:
            end_index = end_index_temp
            print(f"Ending index set to {end_index}\n")    
    except:
        print("Invalid input\n")

    sites = all_sites[start_index:end_index]

    start = time.time()

    print(f"Gathering data from sites...\nThis can take up to 40 minutes depending on the sample size.\n")
    download_all_sites(sites)
    download_time = time.time() - start
    print(f"It took {download_time:.2f} seconds to complete the data scraping\n")
    margin = 20000
    try:
        margin = int(input("Enter the wanted minimum trade margin (default 20000):\n"))
    except:
        pass
    if margin == "":
        margin = 20000

    filtered_list = filter(margin)
    
    with open("FF14_marketdata_remake/trades.txt", "w") as f:
        for item in filtered_list:
            f.write(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Server: {item[3]}, Twintania market price: {item[4]}, URL: {item[5]}\n")
            
    f.close()
    
    duration = time.time() - start
    print(f"Tradeworthy items have been written to trades.txt whole process took {duration:.2f} seconds.")

if __name__ == "__main__":
    main()