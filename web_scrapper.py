import requests
from bs4 import BeautifulSoup
import csv


def scrape_title_price():
    article_tags = soup.find_all("article", attrs={"class": "product_pod"})
    titles_prices = []
    for block in article_tags:

        a_tags = block.find_all("a")
        required_a = a_tags[1]
        title = required_a["title"]

        p_tags = block.find_all("p")
        required_p = p_tags[1]
        price = required_p.text

        title_price = [title,price]
        titles_prices.append(title_price) 
    return titles_prices


with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    header = [["Title", "Price"], []]
    writer.writerows(header)
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    scrape_title_price()
    writer.writerows(scrape_title_price())
    