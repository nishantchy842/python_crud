from blogs.serializers.userSerializers import commentSerializer
from blogs.services.comment_service import commentService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class commentView(APIView):
    def get(self, request, id=None):
        comment = commentService().get_post_comment(post_id=id)
        return Response(comment, status=status.HTTP_200_OK)
    
    def post(self, request):
        service = commentService()
        try:
            comment = service.create_comment(request.data)
            return Response(comment, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)




