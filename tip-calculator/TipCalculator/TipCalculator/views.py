from django.shortcuts import render


def home(request):
    bill = 0
    tip = 0
    people = 0
    if request.method == "POST":
        bill = request.POST['bill']
        tip = request.POST['tip']
        people = request.POST['people']
    
    t = int(tip)/100
    tip_t = int(bill) * t
    T = int(bill) * t
    
    Total = int(bill) + tip_t
    P = 0
    t_e_p = 0
    if people != '' and int(people) > 0:
        P = tip_t / int(people)
        t_e_p = Total / int(people)
        
    p = "$ {0:.2f}".format(P)
    total_each_people = "$ {0:.2f}".format(t_e_p)
    
    tip_total = "$ {0:.2f}".format(T)
    total = "$ {0:.2f}".format(Total)
    
    return render(request,'index.html',{'tip_total':tip_total,'total':total,'tip_people':p,'total_each_people':total_each_people})