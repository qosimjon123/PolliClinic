from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout'),

    path('personal-page/', views.personal_page, name='personal_page'),
    path('register-record/', views.register_record, name='register_record'),
    path('creator-admin-panel/', views.creator_admin_panel, name='creator_admin_panel'),
    path('create-specialization/', views.create_specialization, name='create_specialization'),
]

