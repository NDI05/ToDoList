from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import User

@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def overViews(request):
    api_url ={
        'list':'/listData/',
        'DetailView':'/listDataDetail/',
        'CreateData':'/addData/',
        'UpdateData':'/updateData/',
        'DeleteData':'/deleteData/',
    }
    return Response(api_url)

@api_view(['POST'])
def updateData(request, id):
    users = User.objects.get(id=id)
    serializer = UserSerializer(instance=users ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def listData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listDataDetail(request, id):
    users = User.objects.get(id=id)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteData(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return Response('Succes Delete Data')