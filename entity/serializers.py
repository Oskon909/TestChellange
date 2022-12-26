from entity.models import Entity, Property
from rest_framework import serializers


class EntitySerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Entity
        fields = ["id", "properties", "value", "modified_by"]

    def get_properties(self, obj):
        properties = obj.properties.all()
        properties_dict = {property.key: property.value for property in properties}
        return properties_dict
