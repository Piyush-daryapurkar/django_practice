from django.shortcuts import render,HttpResponse


def index(req):
    movieList={
        'movies':['patalkol','mirjapur','secret games']
    }
    return render(req,"index.html",movieList)

def about(req):
    return render(req,"about.html")










# Create your views here.


# def index(req):                  
#     return HttpResponse("hello this is your home page")

# def about(req):
#     return HttpResponse("this is about page")

# def name(req ,myName):
#     return HttpResponse(f"my name is : {myName}")

# def add(req,num1,num2):
    # return HttpResponse(f"sum is = {num1+num2}")
