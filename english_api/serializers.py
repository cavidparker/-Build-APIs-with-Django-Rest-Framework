from rest_framework import serializers
from .models import Word

# Add Serializer
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'