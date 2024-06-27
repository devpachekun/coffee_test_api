from rest_framework import serializers
from .models import User, UserTransaction, Coffee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','correo','password','is_active','is_superuser','is_staff']


    def create(self, validated_data):
        # Extrae la contraseña del validated_data
        password = validated_data.pop('password')

        # Crea un nuevo usuario sin guardar aún
        user = User(**validated_data)

        # Hashea y establece la contraseña
        user.set_password(password)

        # Guarda el usuario
        user.save()
        
        return user
    
class UserTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = '__all__'

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'