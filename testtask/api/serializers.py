from rest_framework import serializers
from .models import User, Address, Bank


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    bank = BankSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"
