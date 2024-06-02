from django.urls import path
from blogs.views.user import UserViews
from blogs.views.post import postViews
from blogs.views.comment import commentView
from blogs.views.like import CreateLikeView

urlpatterns = [
    path('user/',  UserViews.as_view(), name='user'),
    path('user/<int:id>', UserViews.as_view(), name='user-details'),
    path('post/',  postViews.as_view(), name='post'),
    path('post/<int:id>', postViews.as_view(), name='post-details'),
    path('post/userPost/<int:id>', postViews.as_view(), name='user_post'),
    path('post/comment/<int:id>', commentView.as_view(), name='post_comment'),
    path('post/comment/', commentView.as_view(), name='comment'),
    path('post/like/', CreateLikeView.as_view(), name='create_like'),
]