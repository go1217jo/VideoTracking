from django.shortcuts import render
from django.http import HttpResponse
from . import video_tracking

def index(request):
    #return render(request, 'faceDetection/index.html')
    video_tracking.tracking()
    return HttpResponse(request, "video_tracking")
