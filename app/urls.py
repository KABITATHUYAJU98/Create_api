from django.urls import path
from . import views
from .views import StudentApiView, StudentIdApiView

#api urls
urlpatterns = [
    path('api/students/', StudentApiView.as_view()),
    path('api/students/<int:id>/',StudentIdApiView.as_view()),
]