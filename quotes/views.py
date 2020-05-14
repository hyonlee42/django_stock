from django.shortcuts import render
from .models import Stock

def home(request):
    import requests
    import json
    
    if request.method == 'POST':
      ticker = request.POST['ticker']
      api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3bcd7eb9917441f99e7dab265e023645")

      try:
        api = json.loads(api_request.content)
      except Exception as e:
        api = "Error..."
      return render(request, 'home.html', {'api': api})

    else:
      return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})








def about(request):
  return render(request, 'about.html', {})


def add_stock(request):


  ticker = Stock.objects.all()
  return render(request, 'add_stock.html', {'ticker': ticker})