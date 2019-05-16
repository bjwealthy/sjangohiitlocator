from django.shortcuts import render
from django.http import HttpResponse

from .models import Location


def index (request):   
    location = Location.objects.all()
    context = {
        'data': location
    }
    return render(request, 'index.html', context)


def userDetails(request, user):
    location = 0
    context = {
        'data': location,
        'error': True
    }

    try:
        location = Location.objects.get(foruser=user)        
        context = {
            'data': location,
            'error': False

        }
    except:
        context = {
            'error': True
        }


   

    return render(request, 'userDetails.html', context)

def add(request):
    context = {
        'success': False,
        'message':'',
        'user':''
    }
    if(request.method == 'POST'):
        usernameTemp = request.POST['username']
        IpaddressTemp = request.POST['Ipaddress']


        context['success'] = True
        
        try:
            locationT = Location.objects.get(foruser=usernameTemp)
            IpaddressTemp = IpaddressTemp.replace("[", ',')
            temp = locationT.Ipaddress.replace("]", '') + IpaddressTemp
            locationT.Ipaddress = temp
            locationT.save()
            context['message'] = 'Sucessfully Added more co-ordinates to' + usernameTemp + '\'s history'
            context['user'] = usernameTemp
        except:
            location = Location(foruser=usernameTemp, Ipaddress=IpaddressTemp)
            location.save()
            context['message'] = 'Sucessfully created user ' + usernameTemp
            context['user'] = usernameTemp



    return render(request, 'add.html', context)
