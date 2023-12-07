from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def handler404(request, *args, **argv):
    response = render('404.html')
    response.status_code = 404
    return response