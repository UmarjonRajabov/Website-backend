from rest_framework import serializers
from asosiy.models import Asosiy


class AsosiySerializer(serializers.ModelSerializer):
    number = serializers.CharField()
    class Meta:
        model = Asosiy
        fields = ['number',]


    def create(self, validated_data):
        """
        Create and return a new `Asosiy` instance, given the validated data.
        """
        return Asosiy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance