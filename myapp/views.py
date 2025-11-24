from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def four(request):
    return render(request,'404.html')
def portfolio(request):
    return render(request,'portfolio-details.html')
def service(request):
    return render(request,'service-details.html')
def sarter(request):
    return render(request,'sarter-page.html')


