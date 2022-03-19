from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import GLBModels
from . serializers import glbSerializer
from django.views.decorators.gzip import gzip_page



@gzip_page
def viewpage(request):
    return render(request, 'viewer/index.html')


class ViewData(APIView):
    try:
        def get(self, request, format=None, *args,**kwargs):
            glb_models = GLBModels.objects.get(id=kwargs['pk'])
            serializer = glbSerializer(glb_models, many=False) 
            return Response(serializer.data)
    except Exception as e:
        print(e)