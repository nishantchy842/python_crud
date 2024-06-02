from rest_framework import serializers
from blogs.models.user import userModel
from blogs.models.post import postModel
from blogs.models.comment import commentModel
from blogs.models.like import LikeModel
from blogs.models.tag import tagModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tagModel
        fields = ['id', 'name']

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ['id', 'username','email']
        # fields = '__all__'

        
class commentSerializer(serializers.ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=postModel.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(queryset=userModel.objects.all())

    class Meta:
        model = commentModel
        # fields = ['id', 'title', 'body', 'author', 'created_at']
        fields = '__all__'


    def validate_post_id(self, value):
        if not postModel.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Post not found.")
        return value

    def validate_user_id(self, value):
        if not userModel.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("User not found.")
        return value
    
class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=postModel.objects.all())
    user = userSerializers(read_only=True)  # Include nested user data

    class Meta:
        model = LikeModel
        fields = ['id', 'post', 'user', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user  # Get the authenticated user from the context
        validated_data['user'] = user
        return super().create(validated_data)
    
class PostSerializer(serializers.ModelSerializer):
    author = userSerializers(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=tagModel.objects.all(), source='tags', many=True, write_only=True)

    class Meta:
        model = postModel
        fields = ['id', 'title','body','author', 'like_count', 'likes','tags', 'tag_ids','created_at']

    def get_like_count(self, obj):
        return obj.likes.count()