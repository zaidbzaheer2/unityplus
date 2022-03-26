from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.showcase_page, name='ShowPage'),
    path('case/<str:pk>/',views.viewpage,name='ViewPage'),
    path('api/viewer/data/<str:pk>/',views.ViewData.as_view(), name='view-data'),
    path('test/', views.testpage, name="testPage")

        
]