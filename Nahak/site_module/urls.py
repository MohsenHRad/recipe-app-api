from django.urls import path

from site_module import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('active-account/<active_code>', views.active_account_view, name='active_account'),
]
