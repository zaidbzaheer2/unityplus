from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.viewpage, name='ViewPage'),
    path('api/viewer/data/<str:pk>/',views.ViewData.as_view(), name='view-data')

        
]