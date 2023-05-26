from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug>', views.post, name='post'),
    path('update/<slug>', views.update, name='update'),
    path('delete/<slug>', views.delete, name='delete'),
]
