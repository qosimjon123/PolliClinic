
from django.shortcuts import render
from rest_framework import generics, status
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
    # queryset = Records.objects.all()
    # serializer_class = RecordsGetSerializer
    serializer_class = RecordsGetSerializer

    def get(self, request):
        records = Records.objects.all()
        serializer = RecordsGetSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecordsPostSerializer(data=request.data, context={'request': request})
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': [
                'Запись успешно создана!',
                'Доктор успешно создан!',
                'Специализация успешно создана!',
                'Отзыв на врача успешно создан!',
                'Институт успешно создан!',
                'Направление успешно создано!',
                'Файл PDF успешно загружен!',
                'Результат исследования успешно создан!',
                'Пользователь успешно создан!',
            ],
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'danger',
            'message': ['заполните форму!'],
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class InstitutionView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer



class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Данные пользователя обновлены',
                'data': serializer.data
            })
        return Response({
            'status': 'danger',
            'message': 'Ошибка при обновлении данных',
            'data': serializer.errors
        })



class FilePDFView(generics.ListCreateAPIView):
    queryset = FilePDF.objects.all()
    serializer_class = FilePDFSerializer

class DoctorsReviewsView(generics.ListCreateAPIView):
    queryset = DoctorsReviews.objects.all()
    serializer_class = DoctorsReviewsSerializer
