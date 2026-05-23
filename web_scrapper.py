import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt


def scrape_title_price():
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    article_tags = soup.find_all("article", attrs={"class": "product_pod"})

    titles_prices = []
    for block in article_tags:

        one_book = one_book_detail(block)
        titles_prices.append(one_book)

    return titles_prices


def one_book_detail(block):

    a_tags = block.find_all("a")
    required_a = a_tags[1]
    title = required_a["title"]

    p_tags = block.find_all("p")
    required_p = p_tags[1]
    price = required_p.text
    title_price = [title, price]

    return title_price


def save_csv():
    with open("output.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        header = ["Title", "Price"]
        writer.writerow(header)
        writer.writerows(scrape_title_price())


def plot_graph():
    with open("output.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        titles = []
        prices = []

        for row in reader:
            title = row[0]
            price = float(row[1][2:])
            titles.append(title)
            prices.append(price)
            plt.barh(titles, prices)
        plt.savefig('graph.png')
        plt.show()


def main():

    scrape_title_price()
    save_csv()
    plot_graph()

main()
