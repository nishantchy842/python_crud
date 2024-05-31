from .base import BaseModel
from django.db import models # type: ignore
from .user import userModel

class postModel(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title