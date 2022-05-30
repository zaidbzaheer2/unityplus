from dataclasses import fields
from rest_framework import serializers
from . models import GLBModels

class glbSerializer(serializers.ModelSerializer):
    class Meta:
        model = GLBModels
        fields = ('case_alias','user' ,'id', 'upper_model', 'lower_model', 'upper_stages_number', 'lower_stages_number')