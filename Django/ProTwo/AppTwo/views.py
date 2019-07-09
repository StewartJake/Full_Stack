from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.


def index(request):
    my_dict = {'insert_here':'Go to /users to see the list of user info'}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request):
    usr_list = User.objects.order_by('last_name')
    usr_dict = {'all_users':usr_list}
    return render(request, 'AppTwo/usr.html', context=usr_dict)
