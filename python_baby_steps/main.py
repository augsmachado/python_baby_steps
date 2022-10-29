import requests

from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()

url = 'https://quotes.toscrape.com/tag/love/'


@app.get("/")
async def read_staus():
    return {"staus": "OK", "code": "200"}


@app.get("/quotes")
async def read_quotes():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', attrs={'class': 'text'})

    results = []
    for quote in quotes:
        print(quote.text)
        results.append(quote.text)

    return {"message": "quotes", "results": results}


@app.get('/authors')
async def read_authors():
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    authors = soup.find_all('small', attrs={'class': 'author'})

    results = []
    for author in authors:
        print(author.text)
        results.append(author.text)

    return {"message": "authors", "results": results}
