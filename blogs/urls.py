from django.urls import path
from blogs.views.user import UserViews

urlpatterns = [
    path('user/',  UserViews.as_view(), name='user'),
     path('user/<int:id>', UserViews.as_view())
]