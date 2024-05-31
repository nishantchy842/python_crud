from django.db import models
from .base import BaseModel

class userModel(BaseModel):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.username
    
  
    class Meta:
        verbose_name_plural = "users"