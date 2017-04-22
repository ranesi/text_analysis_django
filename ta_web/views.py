from django.shortcuts import render

def homepage(request):
    return render(request, 'ta_web/base.html', {})
