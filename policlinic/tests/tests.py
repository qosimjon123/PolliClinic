from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from app.models import User, Doctors, Records, Specialization
from django.contrib.auth import get_user_model


class RecordAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_record(self):
        """Тестируем создание записи через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Специализация успешно создана!", response.data["message"])

    def test_get_records(self):
        """Тестируем получение списка записей через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class DoctorsAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_doctor(self):
        """Тестируем создание врача через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Доктор успешно создан!", response.data["message"])

    def test_get_doctors(self):
        """Тестируем получение списка врачей через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class SpecializationAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Специализация успешно создана!", response.data["message"])

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class DoctorsReviewsAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Отзыв на врача успешно создан!", response.data["message"])

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class InstitutionAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Институт успешно создан!", response.data["message"])

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class DirectionAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Направление успешно создано!", response.data["message"])

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class FilePDFAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("Файл PDF успешно загружен!", response.data["message"])

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class ResearchResultsAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/records/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn(
            "Результат исследования успешно создан!", response.data["message"]
        )

    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)


class PolicyAPITest(APITestCase):
    def setUp(self):
        """Подготовка данных для теста"""

        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )

        self.specialization = Specialization.objects.create(
            specialization="Терапевт", description="Описание терапевта"
        )

        self.doctor = Doctors.objects.create(
            user=self.user, specialization=self.specialization
        )

        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

    def test_post_specialization(self):
        """Тестируем создание специализации через API"""

        data = {
            "name_records": "Запись на прием",
            "date_record": "2024-12-01",
            "date_time": "10:00:00",
            "doctor": self.doctor.id,
        }

        response = self.client.post("/api/v1/Policy/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_specializations(self):
        """Тестируем получение списка специализаций через API"""

        Records.objects.create(
            name_records="Запись на прием",
            user=self.user,
            doctor=self.doctor,
            date_record="2024-12-01",
            date_time="10:00:00",
        )

        response = self.client.get("/api/v1/records/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
