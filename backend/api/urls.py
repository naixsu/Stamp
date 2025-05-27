from django.urls import path
from .views import ActiveStampCardListView

urlpatterns = [
    path('active-stampcards/', ActiveStampCardListView.as_view(), name='active-stampcards'),
]
