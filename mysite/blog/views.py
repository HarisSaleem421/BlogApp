# from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, CustomUserSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.views import API_VIEW
# from rest_framework.generics import RetrieveAPIView

# Create your views here.

# class PostDetailAPIView(RetrieveAPIView):
#     queryset = Post.objects.filter(status= Post.Status.PUBLISHED)
#     serializer_class = PostSerializer
#     lookup_field = 'id'

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.published.all()
        serializers = PostSerializer(posts, many = True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET','PATCH','DELETE'])
def post_get(request, id):
    try:
        post = Post.published.get(pk = id)
    except Post.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = PostSerializer(post)
        data = serializer.data
        post.delete()
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def register_user(request):
        serializer = CustomUserSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created Successfully"}, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

