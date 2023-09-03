from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializers



from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get', responses={200: ItemSerializers(many=True)})
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)