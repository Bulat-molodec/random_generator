from django.shortcuts import render
import random
import string
from .forms import RandomAlphanumericForm


def generate_random_alphanumeric(count):
    alphanumeric_characters = string.digits + string.ascii_letters
    random_alphanumeric = ''.join(random.choice(alphanumeric_characters)
                                  for _ in range(count))
    return random_alphanumeric


def index(request):
    form = RandomAlphanumericForm()
    return render(request, 'generator_app/index.html', {'form': form})


def generate(request):
    if request.method == 'POST':
        form = RandomAlphanumericForm(request.POST)
        if form.is_valid():
            number_of_characters = form.cleaned_data['number_of_characters']
            random_alphanumeric_string = generate_random_alphanumeric(number_of_characters)
            response = render(request,
                              'generator_app/result.html',
                              {'random_alphanumeric_string': random_alphanumeric_string})
            response['Cache-Control'] = 'max-age=900, public'
            return response
    else:
        form = RandomAlphanumericForm()

    return render(request, 'generator_app/index.html', {'form': form})
