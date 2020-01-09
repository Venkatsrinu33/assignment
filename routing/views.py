# Create your views here.
from django.shortcuts import render
from rest_framework import status
from routing.serializer import Gatewayserializer,routeserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import *

class Creategateway(APIView):
    def post(self,request):
        serializer=Gatewayserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message":"gateway with same name already exists","params":"name"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "gateway with same name already exists", "params": "name"},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,id):
        sr = Gateway.objects.get(id=id)
        serializer = Gatewayserializer(sr)
        return Response(serializer.data,status=status.HTTP_200_OK)
class route(APIView):
    def post(self,request):
        if request.data.get('prefixes')>99 or request.data.get('prefixes')<9999:
            return Response({"message":"enter correct prefix"},status=status.HTTP_400_BAD_REQUEST)
        serializer=routeserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
                gateway=Gateway.objects.get(id=request.data.get('gateway_id'))
                if gateway!=None:
                    prefixId=Route.objects.get(prefixes=request.data.get('prefixes'))
                    data1= {"id":prefixId.id,"prefix":request.data.get('prefixes'),
                            "gatewayId":{"id":gateway.id,"name":gateway.name,"ipaddresses":gateway.ip_addresses}}
                    return Response({data1}, status=status.HTTP_201_CREATED)
            except:
                return Response({"data": "prefix with same name already exists"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": None},
                            status=status.HTTP_400_BAD_REQUEST)
    def get(self, request,id):
        try:
            sr = Route.objects.get(id=id)
            serializer = routeserializer(sr)
            return Response({"message":"success"},status=status.HTTP_200_OK)
        except:
            return Response({"message":"doesnot exist"},status=status.HTTP_404_NOT_FOUND)

class Search(APIView):
    def get(self,request,number):
        number=str(number)
        num=number[0:4]
        check=Route.objects.filter(prefixes=int(num))
        for checks in check:
            if checks.prefixes==int(num):
                ip = Gateway.objects.get(id=checks.gateway_id)
                return Response({"id":checks.id,"prefix":checks.prefixes,"gateway":{"id":checks.gateway_id,"name":ip.name,"ipaddress":ip.ip_addresses}},status=status.HTTP_200_OK)
            elif checks.prefixes==int(num[0:3]):
                ip=Gateway.objects.get(id=checks.gateway_id)
                return Response({"id":checks.id,"prefix":checks.prefixes,"gateway":{"id":checks.gateway_id,"name":ip.name,"ipaddress":ip.ip_addresses}},status=status.HTTP_200_OK)
            else:
                return Response({"message":"no data found"},status=status.HTTP_404_NOT_FOUND)
        return Response({"message":None},status=status.HTTP_400_BAD_REQUEST)
