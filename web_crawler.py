import requests
from bs4 import BeautifulSoup
import csv

url = "https://vnexpress.net/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h3', class_='title-news')

    with open('vnexpress_articles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])

        for article in articles:
            title = article.text.strip()
            link = article.a['href']
            writer.writerow([title, link])

    print("'vnexpress_articles.csv' da duoc luu.")
