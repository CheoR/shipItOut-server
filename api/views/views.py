from django.shortcuts import render


# Create your views here.
# listener for front-end requests
def index(request):
    # where render is accessing dir templates/
    return render(request, 'index.html')
