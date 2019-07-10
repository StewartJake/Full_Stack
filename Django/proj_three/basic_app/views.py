from django.shortcuts import render
from . import forms


# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')


def form_page_view(request):
    form = forms.norm_form()

    if request.method == 'POST':
        form = forms.norm_form(request.POST)

        if form.is_valid():
            print('Name:', form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Text:', form.cleaned_data['text'])


    return render(request, 'basic_app/form_page.html', {'form': form})

