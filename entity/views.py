from rest_framework import generics
from rest_framework.response import Response

from .models import Entity, User
from .serializers import EntitySerializer


class EnityApiView(generics.ListCreateAPIView):

    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        data = request.POST.get("data[value]")
        exampleData = data if data is not None else 10
        entity = Entity.objects.create(value=exampleData, modified_by=user)
        data = EntitySerializer(entity)
        return Response(data.data)
