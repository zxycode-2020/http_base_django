from django.contrib.auth.models import User
from rest_framework import serializers
from app01.models import Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url','name','age')