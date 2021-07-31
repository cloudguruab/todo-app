from django.urls import path
from . import views

# route our url 
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
]