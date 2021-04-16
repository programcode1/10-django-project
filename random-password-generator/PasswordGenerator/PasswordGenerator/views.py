from django.shortcuts import render
import random

def home(request):
    length = 0
    symbol = ''
    if request.method == 'POST':
        length = request.POST['pwdlength']
        symbol = request.POST.getlist('s')
        
    dict1 = {'lower': 'abcdefghijklmnopqrstuvwxyz', 'upper':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','number':'123456789','symbol':'@!#$%&?'}
    
    
    
    password = ''
    if length != '':
        l = int(length)
        i = 0
        for j in range(l):
            a = symbol[i]
            password += random.choice(dict1[a])
            if i < len(symbol):
                i += 1
            if i == len(symbol):
                i = 0
    else:
        password = "you don't put length of pwd"
    
    return render(request,'index.html',{'password':password})



