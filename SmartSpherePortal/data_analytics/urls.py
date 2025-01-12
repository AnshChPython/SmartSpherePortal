from django.urls import path
from data_analytics import views


urlpatterns = [
    path('data_analytics',views.data_analytics_home,name='data_analytics_home')
]
