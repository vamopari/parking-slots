from django.urls import path

from .views import *


urlpatterns = [
    path('user/registration/', UserViewSet.as_view()),
    path('login/', LoginViewset.as_view()),
    path('user/change-password/', UserChangePassword.as_view()),

]
