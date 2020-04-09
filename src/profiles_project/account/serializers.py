from rest_framework import serializers
from .models import Users


# Serializer To Validated Data [Create, Update] 

class UsersSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'password']

    def create(self, validated_data):
        """Create and return new user."""

        user = Users(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    # def create(self, validated_data):
    #     return Users.objects.create_user(**validated_data)



    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(validated_data['password'])
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance



    #  def update(self, user, validated_data):
    
    #     if "password" in validated_data:
    #         password = validated_data.pop('password')
    #         user.set_password(password)
    #     return super(UsersSerializer, self).update(user, validated_data)