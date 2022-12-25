from .models import Entity, Property
from rest_framework import serializers


class EntisSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = "__all__"


class EntitySerializer12(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Entity
        fields = ["id", "properties", "value", "modified_by"]

    def get_properties(self, obj):
        # obj - экземпляр Entity, для которого генерируется сериализация
        properties = obj.properties.all()
        # создаем словарь с ключами и значениями свойств
        properties_dict = {property.key: property.value for property in properties}
        return properties_dict


class EntitySerializer13(serializers.ModelSerializer):
    value = serializers.IntegerField()
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj):
        # obj - экземпляр Entity, для которого генерируется сериализация
        properties = obj.properties.all()
        # создаем словарь с ключами и значениями свойств
        properties_dict = {property.key: property.value for property in properties}
        return properties_dict

    class Meta:
        model = Entity
        fields = ["id", "properties", "value", "modified_by"]
