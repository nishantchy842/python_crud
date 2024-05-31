from django.urls import path
from blogs.views.user import UserViews
from blogs.views.post import postViews

urlpatterns = [
    path('user/',  UserViews.as_view(), name='user'),
    path('user/<int:id>', UserViews.as_view(), name='user-details'),
    path('post/',  postViews.as_view(), name='post'),
    path('post/<int:id>', postViews.as_view(), name='post-details')
]