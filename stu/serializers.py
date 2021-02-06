__author__ = 'abu'
from rest_framework import serializers
from django.contrib.auth.models import User
from stu.models import school,teacher,student,subject,class_t

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class schoolSerializer(serializers.ModelSerializer):
    school_which_user=UserSerializer()
    password=serializers.CharField(max_length=10,write_only=True)
    confirm_password=serializers.CharField(max_length=10,write_only=True)
    class Meta:
        model=school
        fields=['school_address','school_which_user','password','confirm_password']



    def validate(self, data):
        if data.get("password")!= data.pop("confirm_password"):
            raise serializers.ValidationError("password don't match")
        else:
            return data


    def create(self, validated_data):
        which_data=validated_data.pop("school_which_user")
        password=validated_data.pop("password")
        u=User.objects.create(**which_data)
        u.set_password(password)
        u.save()
        s=school.objects.create(School_which_user=u,**validated_data)
        return s


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=subject
        fields='__all__'

class class_tSerializer(serializers.ModelSerializer):
    class Meta:
        model=class_t
        fields=['class_t_name','class_t_id','class_t_tutor']

