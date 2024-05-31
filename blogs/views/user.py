from rest_framework.views import APIView
from blogs.services.user_services import userServices
from rest_framework import status
from rest_framework.response import Response



class UserViews(APIView):
    def get(self, request, id=None):
        user = userServices()
        if id:
            userById = user.get_single_user(id)
            return Response(userById, status=status.HTTP_200_OK)

        data = user.get_all_users()
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        service_response = userServices().create_user(request.data)
        return Response({"status": service_response["status"], "data": service_response["data"]}, status=service_response["http_status"])
    
    def delete(self, request, id):
        service_response = userServices().delete_user(id)
        return Response({"status": service_response["status"], "message": service_response["message"]}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        serialize_response = userServices().update_user(id,request.data)
        if serialize_response.is_valid():
            serialize_response.save()
            return Response({"status": "success", "data": serialize_response.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serialize_response.errors}, status=status.HTTP_400_BAD_REQUEST)


#permanent delete
    # def delete(self, request, id=None):
    #     item = models.Cars.objects.filter(id=id)
    #     print(item)
    #     item.delete()
    #     return Response({"status": "success", "data": "Item Deleted"})