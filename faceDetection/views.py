from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'C:\\djangoProjects\\Videotracking\\faceDetection\\templates\\faceDetection\\index.html')
