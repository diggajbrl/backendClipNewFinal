from rest_framework import serializers
from .models import Clipath

class ClipathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clipath
        fields = '__all__'