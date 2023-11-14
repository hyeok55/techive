from rest_framework import serializers
from techs.models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password




class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','title', 'company', 'date','url']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','post']

class RegisterSerializer(serializers.ModelSerializer):
    #write only 여서 응답이 올때는 field 에 적용되지 않음
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        #attribute
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"두패스워드가 일치 안합니다"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username= validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields=['username','password','password2']
        extra_kwargs = {'password': {'write_only': True }}








class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tag_name']    

class Post_tagserializer(serializers.ModelSerializer):
    class Meta:
        model = Post_tag
        fields = ['id', 'post', 'tag']

class Compnay_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Tag
        fields = ['id', 'company', 'tag','count', 'updates']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'company_name']