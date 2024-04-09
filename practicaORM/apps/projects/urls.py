from django.urls import path
from .views import ProjectAPIView, TaskAPIView

urlpatterns = [
    path('projects/', ProjectAPIView.as_view()),
    path('projects/<int:project_id>/tasks/', TaskAPIView.as_view())
]