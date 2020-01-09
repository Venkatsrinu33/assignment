from routing.models import Gateway,Route
from rest_framework import serializers

class Gatewayserializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ['id','name','ip_addresses']
class routeserializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['prefixes','gateway_id']