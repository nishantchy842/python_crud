from .base import BaseModel
from django.db import models
from .user import userModel
from .post import postModel

class commentModel(BaseModel):
    comment = models.CharField(max_length=225, null=False)
    post_id = models.ForeignKey(postModel, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self) -> str:
        return self.comment