from django.urls import path
from chatboot import views


urlpatterns = [
    path('chatboot',views.chatboot_home,name='chatboot_home')
]
