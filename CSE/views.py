from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def product(request):
    return render(request, 'product.html')
def service(request):
    return render(request, 'service.html')
def contacts(request):
    return render(request, 'contacts.html')
def aboutus(request):
    return render(request, 'aboutus.html')