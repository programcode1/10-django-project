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
    total_months = 0
    extra_money = 0
    if amount != '' and rate != '' and month != '':
        amount = int(amount)
        rate = float(rate)
        month = int(month)
        interset = (amount *(rate * .01))/month
        monthly = round(((amount / month ) + interset),2)
        total_months = monthly * month
        extra_money = total_months - amount
    monthly = f'$ {monthly}'
    total_months = f'$ {total_months}'
    extra_money = f'$ {extra_money}'
    return render(request,'loan.html',{'ans':monthly,'total_months':total_months,'extra_money':extra_money})