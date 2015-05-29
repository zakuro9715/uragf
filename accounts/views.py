from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
    UpdateView, CreateView
)

from users.models import User

from .forms import RegistrationForm


class UserUpdate(UpdateView):
    fields = ['email', 'username', 'first_name', 'last_name']
    model = User
    template_name = 'accounts/update_form.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        self.object = form.save()
        # Redirect to request.path to change http method to GET
        return HttpResponseRedirect(self.request.path)


class Registration(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/registration_form.html'
    success_url = '/'

    def form_valid(self, form):
        res = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        self.login(username, password)
        return res

    def login(self, username, password):
        user = authenticate(username=username, password=password)
        login(self.request, user)
