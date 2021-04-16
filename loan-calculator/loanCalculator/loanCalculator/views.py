from django.shortcuts import render


def home(request):
    amount = ''
    rate = ''
    month = ''
    if request.method == 'POST':
        amount = request.POST['amount']
        rate = request.POST['rate']
        month = request.POST['month']
    
    monthly = 0
    if amount != '' and rate != '' and month != '':
        amount = int(amount)
        rate = float(rate)
        month = int(month)
        interset = (amount *(rate * .01))/month
        monthly = round(((amount / month ) + interset),2)
    monthly = f'$ {monthly}'
    return render(request,'loan.html',{'ans':monthly})