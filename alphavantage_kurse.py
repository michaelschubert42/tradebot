import requests

def download_kurse():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MBG.DEX&outputsize=full&apikey=demo'
    r = requests.get(url)
    return r.json()
