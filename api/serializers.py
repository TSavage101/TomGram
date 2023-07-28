from rest_framework import serializers
from core.models import Profile, Follow, Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'