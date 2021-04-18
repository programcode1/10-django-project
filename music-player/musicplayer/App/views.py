from django.shortcuts import render
from .models import Song
# Create your views here.
def home(request):
    all_item = Song.objects.all()
    
    return render(request,'index.html',{'item':all_item})




    