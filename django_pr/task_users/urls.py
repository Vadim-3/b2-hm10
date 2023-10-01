from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="task_users/login.html", form_class=LoginForm,
                                     redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(template_name="task_users/logout.html"), name="logout"),

]
