from django.shortcuts import render


def home(request):
    import requests
    import json
    
    #pk_3bcd7eb9917441f99e7dab265e023645
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_3bcd7eb9917441f99e7dab265e023645")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})


def about(request):
  return render(request, 'about.html', {})