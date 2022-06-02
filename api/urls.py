from django.urls import path, include

from accounts.views import Registration

urlpatterns = [
    path('account/registration/', Registration.as_view()),
]
