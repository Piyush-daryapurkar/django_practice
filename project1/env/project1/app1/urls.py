from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    # path('name/<str:myName>/',views.name),
    # path('add/<int:num1>/<int:num2>/',views.add)

 

]

