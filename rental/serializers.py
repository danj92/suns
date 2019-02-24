from rest_framework import serializers
from . import models
# from .models import *


class FriendSerializer(serializers.ModelSerializer):
    # remembering the logged-in user as the owner
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = models.Friend
        fields = ('id', 'name', 'owner')


class BelongingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Belonging
        fields = ('id', 'name')


class BorrowedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned')
