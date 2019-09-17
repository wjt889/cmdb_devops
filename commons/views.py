from django.shortcuts import render

# Create your views here.
def login(request):
    next_url = request.GET.get('next',None)
    

    return render(request,'login.html')