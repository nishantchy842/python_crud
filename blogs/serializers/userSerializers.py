from rest_framework import serializers
from blogs.models.user import userModel
from blogs.models.post import postModel



class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ['id', 'username','email']
        # fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = userSerializers(read_only=True)

    class Meta:
        model = postModel
        # fields = ['id', 'title', 'body', 'author', 'created_at']
        fields = '__all__'
