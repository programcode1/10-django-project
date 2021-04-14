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
    da = datetime.datetime.now()
    hour = int(da.strftime("%I"))
    minute = int(da.strftime("%M"))
    second = int(da.strftime("%S"))
    #fraction 
    secondfraction = second/60
    minutefraction = (secondfraction + minute)/60
    hourfraction = (minutefraction + hour)/12
    #actual degree
    secondrotate = secondfraction *360
    minuterotate = minutefraction *360
    hourrotate = hourfraction *360

    return render(request,'analog_clock.html',{'hr':hourrotate,'mr':minuterotate,'sr':secondrotate})