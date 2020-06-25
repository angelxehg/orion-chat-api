from django.shortcuts import render

from rest_framework import viewsets
from . import models
from . import serializers


class OrganizationViewset(viewsets.ModelViewSet):
    """ Organization Model view set """
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
