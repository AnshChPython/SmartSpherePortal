from django.urls import path
from entertainment import views


urlpatterns = [
    path('entertainment',views.entertainment_home,name='data_analytics_home')
]
