from rest_framework import serializers
from .models import *


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = (
            "created_at",
            "updated_at",
            "package_title",
            "package_description",
            "price",
            "discount",
            "duration",
            "get_absolute_url"
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order,
        fields = (
            "created_at",
            "invoice_no",
            "user",
            "first_name",
            "last_name",
            "cart",
            "grand_total",
            "get_absolute_url",
        )