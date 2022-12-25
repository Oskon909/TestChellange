from django.urls import path

from .views import EnityApiViewCreate, EntityApiView

urlpatterns = [
    path("create", EnityApiViewCreate.as_view(), name="entity"),
    path("list", EntityApiView.as_view(), name="entityList"),
]
