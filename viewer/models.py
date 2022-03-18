from operator import mod
from xml.etree.ElementTree import tostring
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class GLBModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    upper_model = models.FileField(null=True, blank=True)
    lower_model = models.FileField(null=True, blank=True)
    #ipr_form = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.user.username
    # name = models.CharField(blank=True, null=True, max_length=100)
    # age = models.IntegerField(blank=True, null=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    # def __str__(self):
    #     return self.name