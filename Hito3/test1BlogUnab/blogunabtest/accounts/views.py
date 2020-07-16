from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import RegistroUser





class RegistroForm(generic.CreateView):
    model = User
    template_name = 'signup.html'
    form_class = RegistroUser
    success_url = reverse_lazy('login')