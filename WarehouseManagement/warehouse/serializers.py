from rest_framework import serializers
from .models import Products
from .models import Customers
from .models import Suppliers
from .models import Order
from .models import Invoice
from .models import Report
from .models import Warehouse
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['products_name', 'description', 'quantity', 'category', 'price']


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['customer_name', 'phone', 'email', 'country', 'city', 'account_number']


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ['suppliers_name', 'phone_suppliers', 'email_suppliers', 'country_suppliers', 'city_suppliers', 'account_number_suppliers']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_name', 'order_date', 'financial_details', 'delivery_status']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_id', 'amount', 'payment_date', 'customer_or_supplier', 'invoice_date']


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['report_id', 'stored_quantities', 'transfers', 'expenses', 'report_date']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'space', 'storage_capacity']
