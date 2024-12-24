from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from tutorial.quickstart.serializers import GroupSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
