from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blogs.models.user import  userModel
from blogs.models.like import  LikeModel
from blogs.models.post import  postModel
from blogs.serializers.userSerializers import LikeSerializer

class CreateLikeView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = userModel.objects.get(id=user_id)
        except userModel.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        post_id = request.data.get('post_id')
        if not post_id:
            return Response({"error": "post_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            post = postModel.objects.get(id=post_id)
        except postModel.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if LikeModel.objects.filter(post=post, user=user).exists():
            return Response({"error": "Like already exists."}, status=status.HTTP_400_BAD_REQUEST)

        like = LikeModel(post=post, user=user)
        like.save()

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
