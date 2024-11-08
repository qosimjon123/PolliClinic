
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import *
from .serializers import *


def index(request):
    return render(request, "index.html")

class DoctorsView(APIView):
    serializer_class = DoctorSerializer

    def get(self, request):
        doctors = Doctors.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)



class RecordsView(APIView):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer

    def get(self, request):
        records = Records.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecordSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Запись успешно создана!',
                'data': serializer.data
            })

        return Response({
            'status': 'dunger',
            'message': 'заполните форму!',
            'data': serializer.errors
        })



class InstitutionView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilePDFView(generics.ListCreateAPIView):
    queryset = FilePDF.objects.all()
    serializer_class = FilePDFSerializer

class DoctorsReviewsView(generics.ListCreateAPIView):
    queryset = DoctorsReviews.objects.all()
    serializer_class = DoctorsReviewsSerializer
