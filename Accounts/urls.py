from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("profile/", views.profile_get, name="profile"),
    path("profile-post/", views.profile_post, name="profile_post"),
    path("logout/", views.logout_user, name="logout"),
    path("api/user/", views.test_api)
]
