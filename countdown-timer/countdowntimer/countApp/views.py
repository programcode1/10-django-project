from django.shortcuts import render
import time


def home(request):
    day = 0
    hours = 0
    minute = 1

    #convert day to second 
    #second = day * 1440


    #convert day to hour
    #second = hours *3600

    #convert minute to second
    second = minute *60
  
    while second:
        m,s = divmod(second,60)
        timer = "{:02d}:{:02d}:{:02d}:{:02d}".format(day,hours,m,s)
        t = timer
        time.sleep(1)
        second -= 1
        
    print('fire')
    return render(request,'index.html')