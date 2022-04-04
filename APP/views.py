from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.


class GetPackage(APIView):
    def get(self, request):
        try:
            queryset = Package.objects.all()[:3]
            serializer = PackageSerializer(queryset, many=True)
            return Response(serializer.data)
        except Package.DoesNotExist:
            return Http404


class PostPackage(APIView):
    def post(self, request):
        try:
            data = request.data
            package = Package(
                package_title = data["package_title"],
                package_description = data["package_description"],
                price = data["price"],
                discount = data["discount"],
                duration = data["duration"],  
            )
            package.save()
            serializer = PackageSerializer(package, many=True)
            return Response(serializer.data)

        except Package.DoesNotExist:
            return Http404


class EditPackage(APIView):
    def get_object(self, package_id):
        try:
            return Package.objects.get(id=package_id)
        except Package.DoesNotExist:
            return Http404
    
    def post(self, request, package_id):
        data = request.data
        package_obj = self.get_object(package_id)
        package_obj.package_title = data["package_title"]
        package_obj.package_description = data["package_description"]
        package_obj.price = data["price"]
        package_obj.discount = data["discount"]
        package_obj.duration = data["duration"]

        package_obj.save()

        serializer = PackageSerializer(package_obj, many=True)

        return Response(serializer.data)


class GetCart(APIView):
    def get(self, request):
        pass


class PostCart(APIView):
    def post(self, request):
        pass


class GetOrder(APIView):
    def get(self, request):
        pass


class PlaceOrder(APIView):
    def post(self, reuqest):
        pass


class GetOrderDetails(APIView):
    def get(self, request):
        pass