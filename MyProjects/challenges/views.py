from django.http import HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.
my_days = {
    'saturday': 'It is sunny on Saturday',
    'sunday': 'It is sunny on sunday',
    'monday': 'It is sunny on monday',
    'tuesday': 'It is sunny on tuesday',
    'wednesday': 'It is sunny on wednesday',
    'thursday': 'It is sunny on thursday',
    'friday': None

}


def index(request):
    return HttpResponse("Hello, world ; This is my first BackEnd Django project :)")


def saturday(request):
    return HttpResponse("It is Saturday")


def sunday(request):
    return HttpResponse("It is Sunday")


def dynamic_days(request, days):
    # days_data = my_days[days]
    response_data = render_to_string('404.html')

    if days in my_days.keys():
        days_data = my_days.get(days)
        context = {

            "data_1": f'tHE DAY is : {days}',
            "data_2": days_data

        }
        # response_data = f"<h1 style=\"color:red\">It is: {days} and it\'s {days_data}</h1>"
        # response_data = render_to_string('D:\django_Projects\MyProjects\challenges\\templates\challenge.html')
        return render(request, 'D:/django_Projects/MyProjects/challenges/templates/challenge.html', context)

    else:
        raise Http404
        # return HttpResponseNotFound(response_data)
    # return HttpResponseNotFound("This Day is not exist")

    # else:
    #     return HttpResponse(f"Kose nanat {days} :)")


def dynamic_days_by_number(request, days):
    days_name = list(my_days.keys())
    if days > len(days_name):
        return HttpResponseNotFound("404 Fuck You :)")
    redirect_day = days_name[days - 1]
    redirect_url = reverse('days-of-week', args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    # return HttpResponse(days)


def days_list(request):
    days_list_ = my_days.keys()
    context = {
        'data': days_list_
    }
    return render(request, 'D:/django_Projects/MyProjects/challenges/templates/index.html', context)
