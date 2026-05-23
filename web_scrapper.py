import requests
from bs4 import BeautifulSoup
import csv
with open ('output.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    url = "https://books.toscrape.com"
    response = requests.get(url)
    parse = BeautifulSoup(response.text, 'html.parser')
    article_tags = parse.find_all("article", attrs = {"class":"product_pod"})
    for block in article_tags:
        a_tags = block.find_all("a")
        required_a = a_tags[1]
        title = required_a["title"]
        writer.writerow([title])
        

    
 
    


    



