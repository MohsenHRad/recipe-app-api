from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='starting-page'),
    path('post', views.post, name='post-page'),
    path('post/<slug:slug>', views.single_post, name='post-detail-page')

]
