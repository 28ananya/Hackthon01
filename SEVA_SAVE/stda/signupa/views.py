from django.shortcuts import render

# Create your views here.
def signupaaction(request):
    return render(request,"signup_page.html")
