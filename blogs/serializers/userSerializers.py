from rest_framework import serializers
from blogs.models.user import userModel



class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = userModel
        # fields = ['idx', 'username','email']
        fields = '__all__'
