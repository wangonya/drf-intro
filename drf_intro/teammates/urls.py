from django.urls import path
from .views import ListTeamView


urlpatterns = [
    path('team/', ListTeamView.as_view(), name="teammates")
]