from django.urls import path
from first import views

urlpatterns = [
    path('watch/',views.home, name="home"),
    path('underwear/',views.underwear, name="underwear")
]