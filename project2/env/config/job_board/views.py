from django.shortcuts import render,HttpResponse,get_object_or_404

from .models import JobPosting

# Create your views here.


def index(req):
    active_posting=JobPosting.objects.filter(is_active=True)
    context={
        'job_posting': active_posting
    }
    return render(req,'index.html',context)


def job_details(req,pk):
    # job_posting=JobPosting.objects.get(pk=pk)
    job_posting=get_object_or_404(JobPosting,pk=pk,is_active=True)
    context={
        "posting": job_posting
    }
    return render(req,'details.html',context)