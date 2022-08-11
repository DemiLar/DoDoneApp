from account.models import CustomizeUser
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomizeUser
        fields = ['username', 'first_name', 'last_name', 'email', 'work_position', 'id']