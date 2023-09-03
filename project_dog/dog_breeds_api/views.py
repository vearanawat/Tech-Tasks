import requests
from django.shortcuts import render

def fetch(request):
    # Fetch dog breed information from the API
    breed_info_url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(breed_info_url)
    breed_data = response.json().get('message', {})

    return render(request, 'dog_breeds_api/breeds.html', {'breed_data': breed_data})

def random(request, breed_name):
    # Fetch a random image of the selected breed
    random_image_url = f'https://dog.ceo/api/breed/{breed_name}/images/random'
    response = requests.get(random_image_url)
    image_url = response.json().get('message', '')

    return render(request, 'dog_breeds_api/random_image.html', {'image_url': image_url})
