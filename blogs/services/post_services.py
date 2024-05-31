from blogs.models.post import postModel
from blogs.serializers.userSerializers import PostSerializer
from rest_framework import status
from datetime import date

class postServices:
    def get_all_posts(self):
        posts = postModel.objects.all()
        return PostSerializer(posts, many= True).data
    
    def get_single_post(self,id):
        post = postModel.objects.get(id=id)
        return PostSerializer(post).data
    
    def create_post(self, data):
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise Exception(serializer.errors)

    def update_post(self, id, data):
        post = postModel.objects.get(id=id)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            raise Exception(serializer.errors)

    def delete_post(self, id):
        post = postModel.objects.get(id=id)
        post.delete()
        