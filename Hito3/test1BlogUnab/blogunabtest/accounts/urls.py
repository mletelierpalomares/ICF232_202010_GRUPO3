from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.RegistroForm.as_view(), name="signup")

]