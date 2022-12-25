from rest_framework import generics
from rest_framework.response import Response

from .serializer import EntisSerilizer, EntitySerializer12, EntitySerializer13
from .models import Entity, CustomUser


# Create your views here.


class EnityApiViewCreate(generics.CreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntisSerilizer

    def post(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        data = request.POST.get("data[value]")
        exampleData = data if data is not None else 10
        entity = Entity.objects.create(value=exampleData, modified_by=user)
        data = EntitySerializer13(entity)
        return Response(data.data)


class EntityApiView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer12
