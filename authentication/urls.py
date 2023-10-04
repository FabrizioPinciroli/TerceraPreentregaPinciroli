from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("view_profile/", view_profile, name="view_profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
