from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    for x in range(1,10):
        aw = print x
    context ['kiki'] = aw

    return render(request, 'minnim/index.html', context)