from blogs.models.comment import commentModel
from rest_framework.response import Response
from rest_framework import status
from blogs.serializers.userSerializers import commentSerializer



class commentService:
    def get_post_comment(self , post_id):
        comments = commentModel.objects.filter(post_id=post_id)
        comment_serializer  = commentSerializer(comments, many=True).data
        return comment_serializer
    
    def create_comment(self, data):
        print(data)
        serializer = commentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return {"status": "success", "data": serializer.data, "http_status": status.HTTP_200_OK}
        else:
            raise Exception(serializer.errors)