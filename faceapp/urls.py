from django.urls import path
from faceapp.views import Landing, signUp, dashboard



urlpatterns = [
    path("", Landing.as_view(), name= "landingpage"),
    path("signUp", signUp.as_view(), name= "signUpPage"),
    path("dashboard", dashboard.as_view(), name= "dashboard"),
]
