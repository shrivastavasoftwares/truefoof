from django.db import models
from django.contrib.auth.models import User   #first of all apne ko ye line import karani padti hai
# Create your models here.

class school(models.Model):
    school_name=models.CharField(max_length=10,null=True,blank=True)
    school_address=models.CharField(max_length=10,null=True,blank=True)
    school_which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    school_mobile=models.CharField(max_length=10,null=True,blank=True)
    school_id=models.CharField(max_length=10,null=True,blank=True)
    school_img=models.FileField(upload_to='media/img',blank=True,null=True)

gender = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Other", "Other"),
    )
class teacher(models.Model):
    teacher_name=models.CharField(max_length=10,null=True,blank=True)
    teacher_id=models.CharField(max_length=10,null=True,blank=True)
    teacher_email=models.CharField(max_length=10,null=True,blank=True)
    teacher_info=models.CharField(max_length=10,null=True,blank=True)
    teacher_mobile=models.CharField(max_length=10,null=True,blank=True)

class student(models.Model):
    student_name=models.CharField(max_length=10,null=True,blank=True)
    student_id=models.CharField(max_length=10,null=True,blank=True)
    student_class=models.CharField(max_length=10,null=True,blank=True)
    student_mobile=models.CharField(max_length=10,null=True,blank=True)
    student_email=models.CharField(max_length=10,null=True,blank=True)
    student_info=models.CharField(max_length=10,null=True,blank=True)

class subject(models.Model):
    subject_name=models.CharField(max_length=10,unique=True)
    subject_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    subject_teacher_id=models.ForeignKey(teacher,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)


class class_t(models.Model):
    class_t_name=models.CharField(max_length=10,null=True,blank=True)
    class_t_id=models.CharField(max_length=10,null=True,blank=True,unique=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class_t_teacher=models.ManyToManyField(teacher)
    class_t_subject=models.ManyToManyField(subject)
    class_t_tutor=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)



