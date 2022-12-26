from django.urls import path

from .views import EnityApiView

urlpatterns = [
    path('', EnityApiView.as_view()),
]
