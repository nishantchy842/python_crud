from blogs.models import userModel
from blogs.serializers.userSerializers import userSerializers
from rest_framework import status
from datetime import date


class userServices:
    def get_all_users(self):
        user = userModel.objects.all()
        return userSerializers(user, many=True).data
    
    def get_single_user(self, id):
        user = userModel.objects.get(id=id)
        return userSerializers(user).data
    
    def create_user(self,data):
        serializer = userSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return {"status": "success", "data": serializer.data, "http_status": status.HTTP_200_OK}
        else:
            return {"status": "error", "data": serializer.errors, "http_status": status.HTTP_400_BAD_REQUEST}

    def delete_user(self, id):
        user = userModel.objects.get(id=id)
        user.deleted_at = date.today()
        user.is_deleted = True
        user.save()
        return {"status": "success", "message": "User successfully deleted", "data": None}
    
    def update_user(self, id, data):
        print(data)
        item = userModel.objects.get(id=id)
        serializer = userSerializers(item,  data=data, partial=True)
        return serializer
