from rest_framework.views import APIView
from rest_framework.response import Response
from blogs.services.post_services import postServices
from rest_framework import status

class postViews(APIView):
    def get(self, request, id=None):
        service = postServices()
        if id:
            try:
                post = service.get_single_post(id)
                return Response(post, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        posts = service.get_all_posts()
        return Response(posts, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        service = postServices()
        try:
            post = service.create_post(request.data)
            return Response(post, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id=None):
        service = postServices()
        if id:
            try:
                post = service.update_post(id, request.data)
                return Response(post, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error", "data": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
     
    def delete(self, request, id=None):
        service = postServices()
        if id:
            try:
                service.delete_post(id)
                return Response({"status": "success", "data": "Post deleted"}, status=status.HTTP_204_NO_CONTENT)
          
            except Exception as e:
                return Response({"status": "error", "data": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error", "data": "ID not provided"}, status=status.HTTP_400_BAD_REQUEST)   