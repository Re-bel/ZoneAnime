from django.shortcuts import render
from datetime import datetime
from Shop.models import Contact, Animelist, Joggers, Hoodies, Backpacks, Rings, Cosplay, Facemasks
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')

    return render(request, 'contact.html')

def animelist(request):
    lists = Animelist.objects.all()
    return render(request, 'list.html', {'lists': lists})

def hoodies(request):
    hoodies = Hoodies.objects.all()
    return render(request, 'hoodies.html', {'hoodies':hoodies})
    
def joggers(request):
    joggers = Joggers.objects.all()
    return render(request, 'joggers.html', {'joggers':joggers})

def facemasks(request):
    facemasks = Facemasks.objects.all()
    return render(request, 'facemasks.html', {'facemasks':facemasks})

def cosplay(request):
    cosplays = Cosplay.objects.all()
    return render(request, 'cosplay.html', {'cosplays':cosplays})

def backpacks(request):
    backpacks = Backpacks.objects.all()
    return render(request, 'backpacks.html', {'backpacks':backpacks})

def rings(request):
    rings = Rings.objects.all()
    return render(request, 'rings.html', {'rings':rings})
