from django.urls import path
from .views import home, do_logout


urlpatterns = [
    path('', home, name="home"),
    path('logout/', do_logout, name="logout")
]
