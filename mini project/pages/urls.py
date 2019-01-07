from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('contact', views.contact, name='contact'),
    path('stock', views.stockView, name='stockView'),
    path('cloud', views.wordCloud, name='wordCloud'),
    path('<str:pagename>', views.index, name='index'),
]


