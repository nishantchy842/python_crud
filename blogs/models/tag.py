from django.db import models
from .base import BaseModel



class tagModel(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    
  
    