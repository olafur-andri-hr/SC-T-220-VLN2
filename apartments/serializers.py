from rest_framework import serializers
from .models import ApartmentImage, Apartment, ApartmentType, Listing
from location.models import PostalCode
from django.utils.text import Truncator


class PostalCodeSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()

    class Meta:
        model = PostalCode
        exclude = []

    def get_country(self, obj):
        return {
            'name': obj.country.name, 'flag': obj.country.flag,
            'unicode_flag': obj.country.unicode_flag, 'code': obj.country.code
        }


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        exclude = []


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        exclude = []


class ApartmentSerializer(serializers.ModelSerializer):
    apartment_type = ApartmentTypeSerializer()
    apartmentimage_set = ApartmentImageSerializer(many=True)
    postal_code = PostalCodeSerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = (
            'postal_code', 'address', 'apt_number', 'appraisal', 'num_rooms',
            'num_bathrooms', 'size', 'apartment_type', 'description',
            'apartmentimage_set',
        )

    def get_description(self, obj):
        truncator = Truncator(obj.description)
        return truncator.chars(obj.description_truncation_length)


class ListingSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer()

    class Meta:
        model = Listing
        exclude = []
