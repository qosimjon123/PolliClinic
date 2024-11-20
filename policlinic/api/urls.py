from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/doctors/", views.DoctorsView.as_view()),
    path("v1/institution/", views.InstitutionView.as_view()),
    path("v1/records/", views.RecordsView.as_view()),
    path("v1/users/", views.UsersView.as_view()),
    path("v1/user/", views.UserView.as_view()),
    path("v1/doctors/", views.DoctorsView.as_view()),
    path("v1/file-pdf/", views.FilePDFView.as_view()),
    path("v1/doctor-reviews/", views.DoctorsReviewsView.as_view()),
]
