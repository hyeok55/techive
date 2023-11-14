from django.urls import path, include
from .views import *
from . import views




#Generapiview 때문에 <int:id>에서 pk로 수정해줘야함
urlpatterns = [
    path('post/', PostList.as_view(), name='post'),
    #path('post/view/<int:pk>/', IncreasePostView.as_view(), name= 'post-views'),
    #path('post/like/<int:pk>/', IncreasePostLike.as_view(), name= 'post-likes'),
    
    # login
    path('users/', UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]   