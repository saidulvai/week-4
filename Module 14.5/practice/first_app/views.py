from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def index(request):
    return render(request, './first_app/index.html')

def DjangoForm(request):
    form =  contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, './first_app/djangoForm.html', {'form' : form})