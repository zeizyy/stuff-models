from django.shortcuts import render

# start screen view
def start(request):
    return render(request, 'start.html', {})

