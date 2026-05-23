import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

def scrape_title_price(article_tags):
    
    titles_prices = []
    titles= []
    prices = []
    for block in article_tags:

        a_tags = block.find_all("a")
        required_a = a_tags[1]
        title = required_a["title"]
        
        titles.append(title)
        
        p_tags = block.find_all("p")
        required_p = p_tags[1]
        price = required_p.text
        price = float(price[2:])
        prices.append(price)
        
        
        title_price = [title, price]
        titles_prices.append(title_price)
    
    
    plt.barh(titles,prices)
    return titles_prices

with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    header = ["Title", "Price"]
    writer.writerow(header)
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    article_tags = soup.find_all("article", attrs={"class": "product_pod"})

    writer.writerows(scrape_title_price(article_tags))

with open("output.csv", mode = "r", newline= "") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        
plt.show()
        


