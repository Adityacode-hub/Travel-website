from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from datetime import *
from .models import Destination,Contact
# Create your views here.
def index(request):
    # dest=Destination()
    # dest.name='Raygada'
    # dest.desc='the city of mountains'
    # dest.img='destination_1.jpg'
    # dest.price='700'
    # dest.offer=True
    # dest1=Destination()
    # dest1.name='Gunupur'
    # dest1.desc='the city of rush'
    # dest1.img='destination_2.jpg'
    # dest1.price='450'
    # dest1.offer=False
    # dest2=Destination()
    # dest2.name='Parlakhamundi'
    # dest2.desc='keep moving'
    # dest2.img='destination_3.jpg'
    # dest2.price='500'
    # dest2.price=True

    # dest3=Destination()
    # dest3.name='Durgi'
    # dest3.desc='keep moving'
    # dest3.img='destination_4.jpg'
    # dest3.price='500'

    # dest4=Destination()
    # dest4.name='kalahandi'
    # dest4.desc='keep moving'
    # dest4.img='destination_5.jpg'
    # dest4.price='450'

    # dest5=Destination()
    # dest5.name='Koraput'
    # dest5.desc='keep moving'
    # dest5.img='destination_6.jpg'
    # dest5.price='1500'

    # dest6=Destination()
    # dest6.name='kashinagar'
    # dest6.desc='keep moving'
    # dest6.img='destination_7.jpg'
    # dest6.price='100'

    # d=[dest,dest1,dest2]
    d=Destination.objects.all()
    return render(request,'index.html',{'d':d})
def about(request):
    return render(request,'about.html')
def services(request):
     return render(request,'index')
def contact(request):
    if request.method=="POST":
        contact=Contact()
        contact.name=request.POST['Name']
        contact.email=request.POST['email']
        contact.phone=request.POST['phone']
        contact.save()
    
    
    return render(request, 'contact.html')
def news(request):
    return render(request,'news.html')


def destinations(request):
    destinations_data = [
        {
            'name': 'Parlakhamundi',
            'image': 'images/destination_1.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 679
        },
        {
            'name': 'Bhubaneshwar',
            'image': 'images/destination_2.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 579
        },
        {
            'name': 'Raygada',
            'image': 'images/destination_3.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 399
        },
        {
            'name': 'Paris',
            'image': 'images/destination_4.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 639
        },
        {
            'name': 'Gunupur',
            'image': 'images/destination_4.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 929
        },
        {
            'name': 'Palasa',
            'image': 'images/destination_6.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 719
        },
        {
            'name': 'Ranchi',
            'image': 'images/destination_7.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 515
        },
        {
            'name': 'Kuttack',
            'image': 'images/destination_8.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 879
        },
        {
            'name': 'Kolkata',
            'image': 'images/destination_9.jpg',
            'description': 'Nulla pretium tincidunt felis, nec.',
            'price': 679
        },
       
    ]
    
    
    query = request.GET.get('q')
    if query:
        destinations_data = [destination for destination in destinations_data if query.lower() in destination['name'].lower()]
    
    context = {
        'destinations': destinations_data,
        'search_query': query
    }

    return render(request, 'destinations.html', context)
