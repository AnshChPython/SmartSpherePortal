from django.urls import path
from ecommerce import views


urlpatterns = [
    path('ecommerce',views.ecommerce_home,name='ecommerce_home')
]
