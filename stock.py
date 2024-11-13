from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
api_key=os.getenv('API_KEY')

def get_data(stock_symbol):
    url=f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={api_key}"
    response=requests.get(url)
    if response.status_code==200:
       data=response.json()
       return data
    else:
       print (f"error fetching data: {response.status_code}")
       return None

def display_data(data,stock_symbol):
    if 'Global Quote' in data and '05. price' in data['Global Quote'] :
       price=data['Global Quote']['05. price']
       change=data['Global Quote'].get('10. change percent','N/A')
       return {
             'symbol':stock_symbol,
             'price':price,
             'change':change
      }

    else:
       return None


def get_stock_info(stock_symbol):
    data=get_data(stock_symbol)
    if data:
       return display_data(data,stock_symbol)
    else:
       return None
