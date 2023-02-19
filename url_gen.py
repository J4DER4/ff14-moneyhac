import requests as rq
import re

SERVER_LIST = ["Alpha", "Lich", "Odin", "Phoenix", "Raiden", "Shiva", "Zodiark"]

def url_gen():
    #Generate URL'S
    return [f"https://universalis.app/market/{i}" for i in range(36895,40000)]

def test_url():
    #open "urls.txt" and create a session
    f = open("urls.txt", "w")
    session = rq.Session()

    #generate wanted url's
    urls = url_gen()

    # Loop through a url in the url's list, if the session is not an error, write the url to urls.txt
    for i in urls:
        try:
            session.cookies.update({"mogboard_server" : "Shiva", "mogboard_last_selected_server": "Shiva"})
            open_url = session.get(i)

            if open_url.reason != "OK":
                pass

            else:
                f.write(i + "\n")
                print(i)

            open_url.close()

        except:
            pass

    f.close
#test_url()

# Scrapes the integers from the url's and writes them back on the same file *CAUTION*
def minimize_lst():

    with open("urls.txt", "r") as f:
        lines = f.readlines()
    
    for i in range(0, len(lines)):
        lines[i] = re.search(r'\d+', lines[i]).group()

    a = open("urls.txt", "w")
    for i in lines:
        a.write(i + "\n")

    a.close()
#minimize_lst()