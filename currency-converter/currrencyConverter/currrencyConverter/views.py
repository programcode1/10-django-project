from django.shortcuts import render
import requests

def home(request):
    a1 = '-'
    b1 = ' '
    amount = ''
    if request.method == "POST":
        a1 = request.POST["dropdown"]
        b1 = request.POST['drop2']
        amount = request.POST['amount']
    
    ans = ''
    
    if a1 != '' and b1 != '' and amount != '':
        url = 'https://v6.exchangerate-api.com/v6/b3085e6065a637be0f218eb2/latest/'
        resp = requests.get(url+a1)
        currancy_data = resp.json()
        ans = currancy_data['conversion_rates'][b1] * int(amount)
    return render(request,'index.html',{'a':a1,'b':b1,'amount':amount,'ans':ans})


    






