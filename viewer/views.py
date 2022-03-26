import imp
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import GLBModels
from . serializers import glbSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def testpage(request):
    return render(request, 'viewer/test_page.html')
def viewpage(request,pk):
    glb_models = GLBModels.objects.get(id=pk);
    context = {'model': glb_models}
    return render(request, 'viewer/index.html', context);
@login_required(login_url="LoginPage")
def showcase_page(request):
    current_user = request.user
    glb_models = GLBModels.objects.filter(user=current_user)
    context = {'models': glb_models}
    return render(request, 'viewer/showcase.html', context)
    

class ViewData(APIView):
    try:
        def get(self, request, format=None, *args,**kwargs):
            glb_models = GLBModels.objects.get(id=kwargs['pk'])
            serializer = glbSerializer(glb_models, many=False) 
            return Response(serializer.data)
    except Exception as e:
        print(e)