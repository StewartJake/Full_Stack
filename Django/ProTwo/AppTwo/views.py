from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import User_Form

# Create your views here.


def index(request):
    my_dict = {'insert_here':'Go to /signup to signup for news'}
    return render(request, 'AppTwo/help.html', context=my_dict)


def users(request):
    form_dict = {'form':User_Form}

    if request.method == 'POST':
        form = User_Form(request.POST)
        
        if form.is_valid():
            #usr = User.objects.get_or_create(
            #        first_name=form.cleaned_data['first_name'],
            #        last_name=form.cleaned_data['last_name'],
            #        email=form.cleaned_data['email'],)
            # all could have been done:
            form.save(commit=True)
            return index(request
                    )
    return render(request, 'AppTwo/usr.html', context=form_dict)
