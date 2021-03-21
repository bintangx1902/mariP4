from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy as rl
from django.views.generic import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


class ProfileHome(TemplateView):
    template_name = 'member/main.html'
    # model = UserProfile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileHome, self).get_context_data(*args, **kwargs)
        userprofile = UserProfile.objects.get(user_id=self.request.user.id)
        print(userprofile)

        context['userprofile'] = userprofile
        return context

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileHome, self).dispatch(request, *args, **kwargs)


class CreateProfile(CreateView):
    model = UserProfile
    template_name = 'member/create.html'
    form_class = CreateProfileForm
    success_url = rl('profile:home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        a = super(CreateProfile, self).form_valid(form)
        b = HttpResponseRedirect(self.get_success_url())
        return a and b

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(CreateProfile, self).dispatch(request, *args, **kwargs)


class UpdateProfile(UpdateView):
    model = UserProfile
    template_name = 'member/update.html'
    form_class = CreateProfileForm
    success_url = rl('profile:home')

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateProfile, self).dispatch(request, *args, **kwargs)
