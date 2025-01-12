from django.urls import path
from software_solutions import views


urlpatterns = [
    path('solutions',views.software_solutions_home,name='software_solutions_home')
]
