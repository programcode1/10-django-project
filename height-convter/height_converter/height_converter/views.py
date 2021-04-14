from django.shortcuts import render



def home(request):
    f = 0
    i = 0
    c = 0
    if request.method == 'POST':
        f = request.POST['foot']
        i = request.POST['inch']
        c = request.POST['cm']
    ans = None
    if c != '':
        a = int(c)//30.48
        ans = f"{c} cm = {a} foot"
    else:
        a = int(((int(f)*12) + int(i)) *2.54)
        a1 = round(a,1)
        ans = f"{f} ft {i} in = {a1} cm"   
    
    
    return render(request, "index.html",{'ans':ans})
    