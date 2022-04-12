import imp
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import GLBModels, Comment
from . serializers import glbSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def testpage(request):
    return render(request, 'viewer/test_page.html')
def viewpage(request,pk):
    glb_models = GLBModels.objects.get(id=pk);
    if request.method == 'POST':
        content = request.POST.get('comment')
        user = request.user
        case = glb_models
        create_comment = Comment.objects.create(user=user,case=case,content=content)
        if "accept-case" in request.POST:
            glb_models.case_status = 'A'
            glb_models.save()
        elif "reject-case" in request.POST:
            glb_models.case_status = 'R'
            glb_models.save()
        return redirect("HomePage")        

    comments= Comment.objects.filter(case=glb_models)
    context = {'model': glb_models, 'comments': comments}
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