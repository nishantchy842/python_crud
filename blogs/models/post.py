from .base import BaseModel
from django.db import models 
from .user import userModel
from .tag import tagModel

class postModel(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(userModel, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(tagModel, through='PostTag', related_name='posts')


    def __str__(self):
        return self.title
    
    
    
class PostTag(models.Model):
    post = models.ForeignKey(postModel, on_delete=models.CASCADE)
    tag = models.ForeignKey(tagModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'tag')      