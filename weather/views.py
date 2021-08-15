from django.http.response import JsonResponse
from django.shortcuts import render
import json
import urllib.request
from . import variable

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + variable.api_key).read()
            json_result = json.loads(res)
            data = {
                'country_code': str(json_result['sys']['country']),
                'coordinate': str(json_result['coord']['lon']) + ' ' + str(json_result['coord']['lat']),
                'temp': str(json_result['main']['temp']) + 'K',
                'pressure': str(json_result['main']['pressure']),
                'humidity': str(json_result['main']['humidity']),
            }
        except Exception:
            city = ''
            data = ''
            return render(request, 'homepage.html', {'data': data, 'city': city})
    else:
        city = ''
        data = ''
    return render(request, 'homepage.html', {'data': data, 'city': city})