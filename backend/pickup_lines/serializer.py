from rest_framework import serializers
from .models import PickupLines



class PickupLinesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PickupLines
        fields = ('id', 'line', 'cat', 'created')