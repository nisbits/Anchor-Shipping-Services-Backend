from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'designation', 'location', 'rating', 'review_text', 'profile_image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
