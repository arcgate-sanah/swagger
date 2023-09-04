from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Item
from .serializers import ItemSerializers

@swagger_auto_schema(method='get', responses={200: ItemSerializers(many=True)})
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=ItemSerializers)
@api_view(['POST'])
def postData(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201) 
    return Response(serializer.errors, status=400)  