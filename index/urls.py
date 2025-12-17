from django.urls import path
from index import views




urlpatterns = [

    path("home/pepino/cebola", views.home_page , name= "home_page"),
    

]
