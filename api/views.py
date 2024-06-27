from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, UserTransaction, Coffee
from .serializers import UserSerializer, UserTransactionSerializer, CoffeeSerializer, GetUsersSerializer
from rest_framework import permissions, status

from datetime import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id_usuario'] = user.id_usuario
        token['correo'] = user.correo
        token['rol'] = user.rol
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# ==============================

## Vista de register
class UserRegistrationView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==============================

class UserTransactionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserTransactionSerializer

    def post(self, request):
        serializer = UserTransactionSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        lista_transacciones = UserTransaction.objects.all().filter(id_usuario=request.user.id_usuario)
        serializer = UserTransactionSerializer(lista_transacciones, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

class PublicCoffeesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CoffeeSerializer

    def get(self, request):
        coffee_list = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CoffeesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CoffeeSerializer

    def get(self, request):
        coffee_list = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CoffeeSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            coffee = Coffee.objects.get(pk=pk)
        except Coffee.DoesNotExist:
            return Response({'error': 'Coffee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CoffeeSerializer(coffee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            coffee = Coffee.objects.get(pk=pk)
        except Coffee.DoesNotExist:
            return Response({'error': 'Coffee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        coffee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetUsersSerializer

    def get(self, request):
        lista_usuarios = User.objects.all().filter(rol = 'USUARIO')
        serializer = GetUsersSerializer(lista_usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        