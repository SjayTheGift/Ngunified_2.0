from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User

class SignUp(SuccessMessageMixin, generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    success_message = "%(username)s was created successfully"
    template_name = 'signup.html'


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.ListView):
    model = Profile
    template_name = 'profile.html'


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ['image', 'nickname', 'dob', 'gender', 'bio']
    success_message = "Your account has been updated!"
    template_name = 'profile_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('profile_edit', kwargs={
            'pk': self.object.pk,
        })
