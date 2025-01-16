from django.urls import path

from . import views

urlpatterns = [

    # path('saturday', views.saturday),
    # path('sunday', views.sunday),
    path('index', views.index),
    path('<int:days>', views.dynamic_days_by_number),
    path('<str:days>', views.dynamic_days, name='days-of-week'),
    path('', views.days_list, name='days_list')

]
