# noinspection PyUnresolvedReferences
from rest_framework import serializers
from .models import *

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'description']
