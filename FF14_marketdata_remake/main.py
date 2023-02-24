from imports import *
from data_scraper import *
from filters import *

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

    filter()
    with open("FF14_marketdata_remake/trades.txt", "w") as f:
        for item in item_list:
            f.write(f"Item: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Server: {item[3]}, Twintania market price: {item[4]}, URL: {item[5]}\n")
            
    f.close()
    
    duration = time.time() - start
    print(f"Tradeworthy items have been written to trades.txt whole process took {duration:.2f} seconds.")

if __name__ == "__main__":
    main()