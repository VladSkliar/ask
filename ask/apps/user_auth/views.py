from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,
                            password=password)
        if user is None:
            error_msg = ("Provided wrong credentials data")
        else:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('index'))
    else:
        return render_to_response('user_auth/login.html', {}, context)
    return render_to_response('user_auth/login.html',
                              {'username': username,
                               'password': password,
                               'error_msg': error_msg}, context)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = "user_auth/registration.html"

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST['username'],
                            password=self.request.POST['password1'])
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('index'))
