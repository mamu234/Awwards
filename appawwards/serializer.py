from rest_framework import serializers
from .models import Post,Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['sitename', 'url', 'description', 'image']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'prof_pic', 'bio']