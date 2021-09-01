from django.urls import path

from .views import contact_submission_view

urlpatterns = [
    path('', contact_submission_view),
]