from rest_framework import serializers
from .models import Client, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_type', 'balance', 'client']


class ClientSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, required=False)
    class Meta:
        model = Client
        fields = ['id', 'name', 'birth_date', 'city', 'accounts']