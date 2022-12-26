from operator import mod
from xml.etree.ElementTree import tostring
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class GLBModels(models.Model):
    status_list = (
        ("P", "Pending"),("A", "Accepted"),("R", "Rejected"),)
       
    case_alias = models.CharField(null=True, blank=True, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    case_status = models.CharField(max_length=100, choices=status_list,
        default="P")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    upper_model = models.FileField(null=True, blank=True)
    lower_model = models.FileField(null=True, blank=True)
    ipr_form = models.ImageField(null=True, blank=True)
    #ipr_form = models.FileField(null=True, blank=True)

    # name = models.CharField(blank=True, null=True, max_length=100)
    # age = models.IntegerField(blank=True, null=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    # def __str__(self):
    #     return self.name
    upper_stages_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    lower_stages_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    
class Comment(models.Model):
    case = models.ForeignKey(GLBModels, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    content = models.TextField(max_length=150,blank=True, null=True)