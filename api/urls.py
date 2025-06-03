from django.urls import path
from .views import ClipathList

urlpatterns = [
    path('clipath/', ClipathList.as_view(), name='clipath-list')
]