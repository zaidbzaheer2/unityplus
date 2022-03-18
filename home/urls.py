from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.homepage, name='HomePage'),
    path('users/', include('users.urls')),
    path('viewer/', include('viewer.urls'))
        
]