from django.shortcuts import render
from django.http import HttpResponse
from .models import Girl
from rest_framework.viewsets import ModelViewSet
from .serializers import GirlSerializer

# Create your views here.


# def basic(request):
#     return render(request, 'basic.html', {
#         'first_name': 'Maya',
#         'last_name': 'lil',
#         'age': 18
#     })

def basic(request):
    queryset = Girl.objects.all()
    return render(request, 'basic.html', {
        'girls': list(queryset)
    })


class GirlViewSet(ModelViewSet):
    queryset = Girl.objects.all()
    serializer_class = GirlSerializer
