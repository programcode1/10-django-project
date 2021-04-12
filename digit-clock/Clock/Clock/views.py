from django.shortcuts import render
import datetime

def home(request):
    return render(request,'home.html')




def clock(request):
    d = datetime.datetime.today()
    h = d.strftime("%I")
    m = d.strftime("%M")
    p = d.strftime("%p")
    H = f"{h}:{m} {p}"
    
    return render(request,'clock.html',{'h':H})


def analogclock(request):
    return render(request,'analog_clock.html')