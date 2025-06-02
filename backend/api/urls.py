from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StampCardViewSet, StampEntryViewSet

router = DefaultRouter()
router.register(
    r'stamp-cards',
    StampCardViewSet,
    basename='stamp-card',
)
router.register(
    r'stamp-entries',
    StampEntryViewSet,
    basename='stamp-entry'
)

urlpatterns = [
    path('', include(router.urls)),
]
