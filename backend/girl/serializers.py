from rest_framework import serializers
from .models import Girl


class GirlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Girl
        fields = ['id', 'first_name', 'last_name', 'age']
