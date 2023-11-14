from django.shortcuts import render
from rest_framework import generics, permissions
from techs.models import *
from tech_api.serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import views, status


# Create your views here.


#url 나열
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

'''
# view 증가
class IncreasePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = View.objects.all()
    serializer_class = PostViewSerializer

    def get_object(self):
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        return View.objects.get(post=post)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IncreasePostLike(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer

    def get_object(self):
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        return Like.objects.get(post=post)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.likes += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
'''



# url 연결

# 로그인
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class  = RegisterSerializer


