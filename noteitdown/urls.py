from django.urls import path
from . import views
urlpatterns=[
    path('',views.invalid,name="invalid"),
    path('noteitdown/home',views.home,name="home"),
    path('noteitdown/upload',views.upload_view,name='upload'),
    path("noteitdown/about",views.about,name="about"),
]