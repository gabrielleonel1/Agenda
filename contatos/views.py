from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class ContatosView(APIView):
    def get(self, request):
        return render(request, 'home.html')