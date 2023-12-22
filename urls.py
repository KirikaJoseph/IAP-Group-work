
from django.urls import path
from .views import feedback_form, feedback_success

urlpatterns = [
    path('feedback/', feedback_form, name='feedback_form'),
    path('success/', feedback_success, name='success'),
]
