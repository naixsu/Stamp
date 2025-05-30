from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StampCardViewSet

router = DefaultRouter()
router.register(r'stampcards', StampCardViewSet, basename='stampcard')

urlpatterns = [
    path('', include(router.urls)),
]
