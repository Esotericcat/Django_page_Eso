from django.shortcuts import render


def home(request):
    return render(request,'base.html')

def math_prob(request):
    return render(request,'math.html')

# Create your views here.
