from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'body', 'author', 'publish', 'created', 'updated', 'status']

class CustomUserSerialzer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['id','email','first_name','last_name', 'password']
            extra_kwargs = {'password':{'write_only': True}}

        def create(self, validated_data):
            user = CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'], first_name = validated_data.get('first_name', ''), last_name = validated_data.get('last_name', ''))
            return user
     

