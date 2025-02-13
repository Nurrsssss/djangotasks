from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]

    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
#fnjeksdml



 

class Project(models.Model): 

    name = models.CharField(max_length=100) 

    description = models.TextField() 

    start_date = models.DateField() 

    end_date = models.DateField() 

 

    def __str__(self): 

        return self.name 

 

class Category(models.Model): 

    name = models.CharField(max_length=100) 

 

    def __str__(self): 

        return self.name 

 

class Priority(models.Model): 

    level = models.CharField(max_length=50) 

 

    def __str__(self): 

        return self.level 

 

class Task(models.Model): 

    title = models.CharField(max_length=200) 

    description = models.TextField() 

    project = models.ForeignKey(Project, on_delete=models.CASCADE) 

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 

    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True) 

    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 

    due_date = models.DateField() 

 

    def __str__(self): 

        return self.title 
    
class Contact(models.Model): 

    name = models.CharField(max_length=100) 

    email = models.EmailField() 

    message = models.TextField() 

class CV(models.Model): 

    name = models.CharField(max_length=255) 

    email = models.EmailField() 

    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) 
