from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import GLBModels, Comment
from . serializers import glbSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
import datetime
from django.template.loader import render_to_string
def sendMail(body, reciever):
    email = EmailMessage(
        'Case Review',
        body,
        settings.EMAIL_HOST_USER,
        [reciever],
    )
    email.fail_silently = False
    email.send()

def testpage(request):
    return render(request, 'viewer/test_page.html')
@login_required(login_url="LoginPage")
def viewpage(request,pk):
    current_url = request.build_absolute_uri()
    
    glb_models = GLBModels.objects.get(id=pk)
    
    if request.method == 'POST':
        content = request.POST.get('comment')
        user = request.user
        case = glb_models
        create_comment = Comment.objects.create(user=user,case=case,content=content)
        if "accept-case" in request.POST:
            glb_models.case_status = 'A'
        elif "reject-case" in request.POST:
            glb_models.case_status = 'R'
        context = {
        'name': glb_models.user.username,
        'checker_name': request.user.username,
        'status': glb_models.get_case_status_display(),
        'case_alias': glb_models.case_alias,
        'date': datetime.datetime.now(),
        'case_id': glb_models.id,
        'case_link': current_url,
        'remarks': content,
    }
        email_body = render_to_string('email-body.html', context)
        glb_models.save()
        sendMail(email_body, glb_models.user.username)
        return redirect(f"{current_url}")        

    comments= Comment.objects.filter(case=glb_models)
    context = {'model': glb_models, 'comments': comments}
    return render(request, 'viewer/index.html', context);
@login_required(login_url="LoginPage")
def showcase_page(request):
    current_user = request.user
#    glb_models = GLBModels.objects.filter(user=current_user)
    glb_models = GLBModels.objects.all()
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