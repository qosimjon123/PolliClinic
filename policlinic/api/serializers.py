from django.db import models
from rest_framework import serializers

from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'policy']
        # fields = '__all__'

class UserDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email']
        # fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['specialization', 'description']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserDoctorSerializer()
    specialization = SpecializationSerializer()

    class Meta:
        model = Doctors
        fields = ['user', 'specialization']


class RecordsGetSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    user = UserSerializer()

    class Meta:
        model = Records
        fields = '__all__'

class RecordsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['name_records', 'date_create', 'date_record', 'date_time', 'doctor']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Records.objects.create(**validated_data)


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class FilePDFSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    def get_file_url(self, obj):
        return obj.file_path.url

    class Meta:
        model = FilePDF
        fields = ['name_file', 'file_url']


class DoctorsReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsReviews
        fields = '__all__'