from django.shortcuts import render


def index(request):
    return render(request, 'blog/templates/blog/index.html')


def post(request):
    pass


def single_post(request):
    pass
