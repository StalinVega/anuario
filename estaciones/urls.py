from django.urls import path,include
from rest_framework.routers import DefaultRouter

# Views
from estaciones import views

router = DefaultRouter()
router.register(r'estaciones', views.GetAllEstaciones, basename='estaciones')


urlpatterns=[
    
    path('', include(router.urls)),

]