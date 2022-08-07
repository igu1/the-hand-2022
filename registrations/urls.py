from django.urls import path
from .views import *

urlpatterns = [
    path('in', login_view, name='login'),
    path('out', logout_view, name='logout'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('registration', register_user, name='registration'),
]
