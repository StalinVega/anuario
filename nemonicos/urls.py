from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from nemonicos import views 

router = DefaultRouter()
router.register(r'humedad', views.GetHumedad, basename='humedad')


urlpatterns=[
    
    path('', include(router.urls)),

]