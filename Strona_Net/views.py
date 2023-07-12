from django.shortcuts import render
import math
from django.views import View


def home(request):
    return render(request, 'base.html')


class PrimeView(View):
    def get(self, request):
        return render(request, 'primes.html')

    def post(self, request):
        first_number = int(request.POST.get('first'))
        second_number = int(request.POST.get('second'))
        check_prime = get_prime_numbers(first_number, second_number)
        vis = visualize_numbers(check_prime)

        return render(request, 'primeview.html', {'result': vis})



def visualize_numbers(numbers):
    for number in numbers:
        print("*" * number)
# Create your views here.
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


def visualize_numbers(numbers, symbol='#'):
    max_number = max(numbers)
    num_digits = len(str(max_number))

    visualizations = []
    for i, number in enumerate(numbers, start=1):
        label = f'Number {i}:'
        bar = symbol * number
        visualization = f'{label:<10} {bar:{symbol}<{max_number * num_digits}}'
        visualizations.append(visualization)

    return visualizations
