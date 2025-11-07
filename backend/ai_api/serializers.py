from rest_framework import serializers
from .models import Enhancement

class EnhancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enhancement
        fields = '__all__'