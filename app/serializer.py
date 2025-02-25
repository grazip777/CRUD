from rest_framework import serializers

from app.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        date = serializers.DateTimeField(read_only=True)

        class Meta:
            model = UserInfo
            fields = "__all__"

        def create(self, validated_data):
            return UserInfo.objects.create(**validated_data)
