from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer


class ListTeamView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

