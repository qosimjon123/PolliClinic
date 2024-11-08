from django.db import models
from rest_framework import serializers

from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'username', 'first_name', 'last_name', 'middle_name', 'email', 'policy', 'password']
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


class RecordSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctors.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Records
        fields = '__all__'

    def create(self, validated_data):
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