from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    api_request=requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api=json.loads(api_request.content)
    price_request=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR')
    price=json.loads(price_request.content)
    return render(request, 'home.html', {'api':api, 'price':price})

def prices(request):
    if request.method=='POST':
        quote=request.POST['quote']
        quote=quote.upper()
        crypto_request=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD,EUR')
        crypto=json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        not_found='Enter a valid quote!'
        return render(request, 'prices.html', {'not_found':not_found})