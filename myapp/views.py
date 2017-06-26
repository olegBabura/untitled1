from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
import requests
from .forms import InputForm


def get_wind_direction(deg):
    l = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']
    for i in range(0, 8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res


def landing(request):
        return render(request, 'landing.html')


def error404(request):
    return render(request, 'error404.html')



def check_existance_in_db(s_city):
    try:
        checker = City.objects.get(city_name=s_city)
        return True
    except:
        return False


def get_name(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['u_city']
            # checking for existancce in database
            if check_existance_in_db(city):

                # if exist printing from bd
                try:
                    return render(request, 'index.html', {
                        'form': form,
                        'db_city': City.objects.filter(city_name=city)[0],
                        'db_forecast0': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[0],
                        'db_forecast1': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[1],
                        'db_forecast2': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[2],
                        'db_forecast3': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[3],
                        'db_forecast4': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[4],
                        'image0': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[0].conditions + ".svg",
                        'image1': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[1].conditions + ".svg",
                        'image2': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[2].conditions + ".svg",
                        'image3': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[3].conditions + ".svg",
                        'image4': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[4].conditions + ".svg",
                        'state': "from db",
                    })
                except Exception as e:
                    print("Exception (database):", e)
                    return HttpResponseRedirect('/error404/')
                    pass
            else:
                # if not exist
                # getting city id
                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                   params={'q': city, 'type': 'like', 'units': 'metric',
                                           'APPID': "3e593b0d5a6c511ae11d069ed5c42860"})
                    data = res.json()
                    city_id = data['list'][0]['id']

                    # getting json file from api
                    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                                   params={'id': city_id, 'units': 'metric', 'lang': 'en',
                                           'APPID': "3e593b0d5a6c511ae11d069ed5c42860"})
                    data = res.json()

                    # adding city table
                    t_city = City(
                        city_name=city,
                        lat=data['city']['coord']['lat'],
                        lon=data['city']['coord']['lon'],
                    )
                    t_city.save()

                    # adding 5 forecast tables
                    i = 0
                    while i < 40:
                        t_forecast = Forecast(
                            city_id=t_city,
                            date=(data['list'][i]['dt_txt'])[:10],
                            temp='{0:+3.0f}'.format(data['list'][i]['main']['temp']),
                            wind_speed='{0:2.0f}'.format(data['list'][i]['wind']['speed']) + " m/s",
                            wind_direction=get_wind_direction(data['list'][i]['wind']['deg']),
                            conditions=data['list'][i]['weather'][0]['main'],
                        )
                        t_forecast.save()
                        i += 8

                    return render(request, 'index.html', {
                        'form': form,
                        'db_city': City.objects.filter(city_name=city)[0],
                        'db_forecast0': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[0],
                        'db_forecast1': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[1],
                        'db_forecast2': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[2],
                        'db_forecast3': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[3],
                        'db_forecast4': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[4],
                        'image0': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[0].conditions + ".svg",
                        'image1': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[1].conditions + ".svg",
                        'image2': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[2].conditions + ".svg",
                        'image3': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[3].conditions + ".svg",
                        'image4': Forecast.objects.filter(city_id=City.objects.filter(city_name=city))[4].conditions + ".svg",
                        'state': "from api",
                    })
                except Exception as e:
                    print("Exception (forecast):", e)
                    return HttpResponseRedirect('/error404/')
                    pass
                #return HttpResponseRedirect('/landing/')
    else:
        form = InputForm()
    try:
        return render(request, 'index.html', {
            'form': form,
            'db_city': City.objects.filter(id=1)[0],
            'db_forecast0': Forecast.objects.filter(city_id=City.objects.filter(id=1))[0],
            'db_forecast1': Forecast.objects.filter(city_id=City.objects.filter(id=1))[1],
            'db_forecast2': Forecast.objects.filter(city_id=City.objects.filter(id=1))[2],
            'db_forecast3': Forecast.objects.filter(city_id=City.objects.filter(id=1))[3],
            'db_forecast4': Forecast.objects.filter(city_id=City.objects.filter(id=1))[4],
            'image0': Forecast.objects.filter(city_id=City.objects.filter(id=1))[0].conditions + ".svg",
            'image1': Forecast.objects.filter(city_id=City.objects.filter(id=1))[1].conditions + ".svg",
            'image2': Forecast.objects.filter(city_id=City.objects.filter(id=1))[2].conditions + ".svg",
            'image3': Forecast.objects.filter(city_id=City.objects.filter(id=1))[3].conditions + ".svg",
            'image4': Forecast.objects.filter(city_id=City.objects.filter(id=1))[4].conditions + ".svg",
            'state': "from db",
        })
    except Exception as e:
        print("Exception (pre_load):", e)
        return render(request, 'index.html', {'form': form})
        pass