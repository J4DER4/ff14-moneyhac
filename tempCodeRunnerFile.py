for entry in itemprice:
   if(entry.find("td", class_="price-current")):
       price = entry.find("td", class_="price-current")