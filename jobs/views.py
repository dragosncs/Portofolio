from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):  #functia dragos 
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs}) #returneaza prin cerere folderul jobs fisierul HTML

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id) #primary key for evrey model
    return render(request, 'jobs/detail.html', {'job':job_detail})