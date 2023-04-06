from django.contrib.auth import views
from django.urls import reverse_lazy


class UserLoginView(views.LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(views.LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
