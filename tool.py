import requests
from bs4 import BeautifulSoup
import scrape_tool
import sys
import time
def main():

    url_list = ""
    url_list = open("urls.txt", "r")
    output_list = []
    #sys.stdout = open("data.txt", "w")

    test_rounds = 10
    i = 0
    target = "Twintania"
    start = time.time()
    count = 0
    for line in url_list:
        count += 1
        x = scrape_tool.scrape(target, line)
        print(f"COUNT: {count} --- {x}")
        output_list.append(x)
    print(output_list)
    end = time.time()
    print(end - start)


    url_list.close()
    #sys.stdout.close()


main()