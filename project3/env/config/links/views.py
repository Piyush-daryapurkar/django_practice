from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.urls import reverse

from .models import Link
# Create your views here.
def index(request):
    links=Link.objects.all()
    context={
        'links':links
    }
    return render(request, 'index.html',context)
 
def root_link(request ,link_slug):
    link=get_object_or_404(Link,slug=link_slug)
    link.click() #incriment click field

    return redirect(link.url)

