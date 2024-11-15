from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, CharField, DateField, Model, CASCADE, ForeignKey, SET_NULL
from django.core.files.storage import FileSystemStorage


class Policy(models.Model):
    policy_number = models.IntegerField(verbose_name="Полис")
    date_receipt = models.DateField(auto_now=True, verbose_name="дата получения")
    confirmed = models.BooleanField(default=False, verbose_name="подтвержденый")

    def __str__(self):
        return str(self.policy_number)

    class Meta:
        verbose_name = "Полис"
        verbose_name_plural = "Полиса"


class User(AbstractUser):
    middle_name = models.CharField(max_length=30, default=None, blank=True, null=True, verbose_name="Отчество")
    policy = models.OneToOneField(Policy, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Полис")

    def __str__(self):
        if self.middle_name == "":
            return self.first_name + " " + self.last_name + "."
        else:
            return str(self.first_name) + " " + str(self.last_name) + "." + str(self.middle_name) + "."

    def save(self, *args, **kwargs):
        # Check if the password is set and not already hashed
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Specialization(models.Model):
    specialization = models.CharField(max_length=100, unique=True, verbose_name="Специализация")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.specialization

    class Meta:
        verbose_name = "Название специализации"
        verbose_name_plural = "Специализации"


class Doctors(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, verbose_name="Пользователь")
    specialization = ForeignKey(Specialization, on_delete=SET_NULL, null=True, verbose_name="Специализация")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.user.middle_name + " - " + self.specialization.specialization

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Докторы"


class DoctorsReviews(models.Model):
    date = models.DateField(auto_now=True, verbose_name="Дата создания")
    description = models.TextField(default=None, verbose_name="Описание")
    raiting = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Рейтинг") # максимум 5
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Пользователь")
    doctor = models.ForeignKey(Doctors, on_delete=CASCADE, verbose_name="Доктор")

    def __str__(self):
        return "отзыв от " + str(self.user) + " на доктора " + str(self.doctor)

    class Meta:
        verbose_name = "Отзыв на врача"
        verbose_name_plural = "Отзывы на врачей"

#class UserRole
#class BrowsingHistory

class Institution(models.Model):
    name_institution = models.CharField(max_length=255, verbose_name="Название института")
    description = models.TextField(verbose_name="Описание института")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    def __str__(self):
        return self.name_institution

    class Meta:
        verbose_name = "Институт"
        verbose_name_plural = "Институты"


# направление
class Direction(models.Model):
    name_direction = models.CharField(max_length=255, verbose_name="Название направления")
    until_time = DateField(verbose_name="дата посещения")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    institution = models.OneToOneField(Institution, on_delete=models.SET_NULL, null=True, default=None, verbose_name="Название учреждения")

    def __str__(self):
        return "Направление " + self.name_direction + " для " + str(self.user) + " на время " + str(self.until_time)

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class FilePDF(models.Model):
    name_file = models.CharField(max_length=255, verbose_name="Название файла")
    file_path = models.FileField(verbose_name="Путь к файлу", upload_to="pdf")

    def __str__(self):
        return str(self.file_path)

    def delete(self, *args, **kwargs):

        storage, path = self.file_path.storage, self.file_path.path

        super(FilePDF, self).delete(*args, **kwargs)
        try:
            storage.delete(path)
        except Exception as e:
            print(f'ошибка при удалении файла по пути {path}: {e}')

    class Meta:
        verbose_name = "Файл PDF"
        verbose_name_plural = "Файлы PDF"


class ResearchResults(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, default=None, verbose_name="Пользователь")
    name_research = models.CharField(max_length=100, verbose_name="Название исследования")
    date = models.DateField(auto_now=True, verbose_name="Дата исследования")
    file_path = models.OneToOneField(FilePDF, on_delete=CASCADE, verbose_name="Путь к файлу")
    institution = models.OneToOneField(Institution, on_delete=models.SET_NULL, null=True, default=None, verbose_name="Название института")

    def __str__(self):
        return self.name_research

    class Meta:
        verbose_name = "Результаты исследования"
        verbose_name_plural = "Результаты исследований"

#Таблица с возможными записями
class Records(models.Model):
    name_records = models.CharField(max_length=100, default="Запись")
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name="Пользователь")
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True, verbose_name="Доктор")
    date_create = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    date_record = models.DateField(auto_now_add=True, verbose_name="День записи")
    date_time = models.TimeField(default=None, verbose_name="Время записи")

    def __str__(self):
        return self.name_records

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"