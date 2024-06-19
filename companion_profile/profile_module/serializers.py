from rest_framework import serializers
from .models import Companion_profile

class CompanionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companion_profile
        fields = '__all__'