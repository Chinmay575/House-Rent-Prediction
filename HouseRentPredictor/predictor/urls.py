from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('predictor/',views.predictor,name ='predictor'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('predict/',views.predict,name='predict'),
    path('dataset/',views.link2dataset,name='dataset'),
    path('notebook/',views.link2notebook,name='notebook')
]
