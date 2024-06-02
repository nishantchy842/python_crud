from .base import BaseModel
from django.db import models
from .user import userModel
from .post import postModel

class LikeModel(BaseModel):
    post = models.ForeignKey(postModel, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'