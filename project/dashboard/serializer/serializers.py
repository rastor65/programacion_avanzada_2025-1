from rest_framework import serializers
from dashboard.models import *

class clientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('id' , 'name', 'phone', 'email', 'document_id', 'address', 'creation_date', 'is_active')
        read_only_fields = ('creation_date', )

class suppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = suppliers
        fields = ('id' , 'name', 'contact_name', 'phone', 'email', 'address', 'creation_date', 'is_active')
        read_only_fields = ('creation_date', )

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('id' , 'category', 'name', 'description', 'stock', 'cost_price', 'sale_price', 'ID_supplier', 'is_active')
