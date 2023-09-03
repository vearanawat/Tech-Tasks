from django.http import JsonResponse
import json

def Final(request):
    start = int(request.GET.get('start', 1))
    end = int(request.GET.get('end', 100))
    result = {}
    for num in range(start, end ):
        if prime(num):
            result[num] = bin(num)[2:]
        else:
            result[num] = div(num)
    
    return JsonResponse(result)

def prime(num):
    flag = False
    if num == 1:
        flag = False
    elif (num > 2):
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
            else:
                flag = True
    elif (num == 2):
        flag = True
    return flag

#find divisors:
def div(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

