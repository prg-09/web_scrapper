import requests
from bs4 import BeautifulSoup
import csv

def fetch_title():
    
    article_tags = soup.find_all("article", attrs = {"class":"product_pod"})
    for block in article_tags:
        a_tags = block.find_all("a")
        required_a = a_tags[1]
        title = required_a["title"]
        
        writer.writerow([title])
    return(title)
       
         
with open ('output.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    header = ['Title', 'Price']    
    writer.writerow(header)
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    fetch_title()
    
    
 
    
    
   
        
        

    
 
    


    



