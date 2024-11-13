from flask import Flask,render_template,request
from dotenv import load_dotenv
import os
import requests
from stock import get_stock_info


app=Flask(__name__)
load_dotenv()
api_key=os.getenv('API_KEY')

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/stock')
def stock():
   stock_symbol=request.args.get('symbol')
   if not bool(stock_symbol.strip()):
      return render_template('stock_not_found.html')

   else:
      stock_data=get_stock_info(stock_symbol)
      print (stock_data)
      if stock_data:
         return render_template('stock.html',stock_data=stock_data)
      else:
         return render_template('stock_not_found.html')

if __name__=="__main__":
   app.run(debug=True,host='0.0.0.0',port=5000)




