from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def personal_page(request):
    return render(request, 'personal_page.html')

def edit_personal_date(request):
    return  render(request, 'personal_page.html')

def register_record(request):
    return render(request, 'register_record.html')

def creator_admin_panel(request):
    return render(request, 'creator_admin_panel.html')


def create_specialization(request):
    if request.method == "POST":
        try:
            specialization_name = request.POST["specialization_name"]
            if specialization_name == "":
                messages.warning(request, "Поле названия должно быть обязательным")
                return redirect('creator_admin_panel')
            if len(specialization_name) <= 3:
                messages.warning(request, "название для специализации должно быть больше 3 букв")
                return redirect('creator_admin_panel')

            specialization_description = request.POST["specialization_description"]
            specialization = Specialization.objects.create(specialization=specialization_name, description=specialization_description)
            specialization.save()
            messages.success(request, "Специализация успешно создана")
        except Exception  as e:
            print(type(e))
            messages.error(request, "Такая специализация уже существует")

        return redirect('creator_admin_panel')

