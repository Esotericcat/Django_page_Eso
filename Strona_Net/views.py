from django.shortcuts import render
import math
from django.views import View
def home(request):
    return render(request,'base.html')

def prime_prob(request):
    def get(self,request):
        return render(request, 'primes.html')
    def post(self,request):
        first_number = request.POST.get('first')
        second_number = request.POST.get('second')
        check_prime = get_prime_numbers(first_number,second_number)



class PrimeView(View):



def calculate_trigonometric_functions(angle_in_radians):
    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    tan_value = math.tan(angle_in_radians)

    return sin_value, cos_value, tan_value

def get_prime_numbers(start, end):
    prime_numbers = []

    for num in range(start, end + 1):
        if num > 1:
            # Check for factors
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)

    return prime_numbers


# Create your views here.
