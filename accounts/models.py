from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)
    ROLE_CHOICES=(
        ("trainer","trainer"),
        ("student","student")
    )
    role=models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")

class TrainerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer_profile",
    )
    bio = models.TextField(blank=True,null=True)
    qualification=models.CharField(max_length=200,null=True)
    subject_expertise = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    employee_id = models.CharField(max_length=255,null=True)
    department=models.CharField(max_length=200,null=True)
    designation=models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TrainerProfile: {self.user.username}"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    student_id=models.CharField(max_length=200,null=True)
    date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=100,null=True)
    qualification=models.CharField(max_length=200,null=True)
    institution=models.CharField(max_length=200,null=True)
    course=models.CharField(max_length=200,null=True)
    academic_year=models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"StudentProfile: {self.user.username}"

from django.db.models.signals import post_save

def create_trainer_profile(sender,instance,created,**kwargs):
    
    if created and instance.role=="trainer":

     TrainerProfile.objects.create(user=instance)
post_save.connect(create_trainer_profile,sender=User)

def create_student_profile(sender,instance,created,**kwargs):
    if created and instance.role=="student" :
        StudentProfile.objects.create(user=instance)
post_save.connect(create_student_profile,sender=User)



    
