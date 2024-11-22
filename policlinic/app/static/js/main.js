const serverUrl = "http://127.0.0.1:8000/";


function loadDoctors() {
    fetch(`${serverUrl}api/v1/doctors/`)
        .then(response => response.json())
        .then(doctors => {
            const doctorSelect = document.getElementById('doctor-select');
            doctorSelect.innerHTML = '<option value="" disabled selected>Выберите врача</option>';

            doctors.forEach(doctor => {
                const option = document.createElement('option');
                option.value = doctor.user.id;
                const doctorName = `${doctor.user.first_name} ${doctor.user.last_name}`;
                const specialization = doctor.specialization.specialization;

                option.textContent = `${doctorName} (${specialization})`;
                doctorSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Ошибка при загрузке списка докторов:", error);
            const doctorSelect = document.getElementById('doctor-select');
            doctorSelect.innerHTML = '<option value="" disabled>Не удалось загрузить врачей</option>';
        });
}

function loadUserPersonalPage() {
    fetch(`${serverUrl}api/v1/user/`)
        .then(response => response.json())
        .then(user => {
            document.getElementById('username').value = user.username;
            document.getElementById('first_name').value = user.first_name;
            document.getElementById('last_name').value = user.last_name;
            document.getElementById('middle_name').value = user.middle_name;
            document.getElementById('email').value = user.email;
        })
        .catch(error => {
            console.error('Error loading user data:', error);
        });
}

window.addEventListener('DOMContentLoaded', loadUserPersonalPage);
window.addEventListener('DOMContentLoaded', loadDoctors);


function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return null;
}

// Проверяем, что элемент с ID 'personal-page' существует
const personalPageForm = document.getElementById('personal-info');
if (personalPageForm) {
    personalPageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const personalDataToSend = {
            username: formData.get('username'),
            first_name: formData.get('first_name'),
            last_name: formData.get('last_name'),
            middle_name: formData.get('middle_name'),
            email: formData.get('email'),
        };

        fetch(`${serverUrl}/api/v1/user/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(personalDataToSend)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showAlert(data.message, 'success');
            } else {
                showAlert(data.message, 'danger');
            }
        })
        .catch(error => {
            showAlert('Произошла ошибка при отправке данных.', 'danger');
        });
    });
}

// Проверяем, что элемент с ID 'recordForm' существует
const recordForm = document.getElementById('record-form');
if (recordForm) {
    recordForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const recordData = {
            name_records: formData.get('name_records'),
            doctor: formData.get('doctor'),
            date_record: formData.get('date'),
            date_time: formData.get('time'),
            date_create: new Date().toISOString()
        };

        fetch(`${serverUrl}api/v1/records/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(recordData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Выводим только первое сообщение в случае успеха
                showAlert(data.message[0], 'success');
            } else {
                // Выводим все сообщения в случае ошибки
                showAlert(data.message, 'danger');
            }
        })
        .catch(error => {
            showAlert('Произошла ошибка при отправке данных.', 'danger');
        });
    });
}




function showAlert(message, type) {
    const messageContainer = document.getElementById('alert-container');

    // Создаем элемент alert
    const newAlert = document.createElement('div');
    newAlert.classList.add('alert', 'alert-' + type, 'alert-dismissible', 'fade', 'show');
    newAlert.setAttribute('role', 'alert');

    // Добавляем сообщение
    newAlert.textContent = message;

    // Создаем кнопку для закрытия
    const closeButton = document.createElement('button');
    closeButton.setAttribute('type', 'button');
    closeButton.setAttribute('class', 'btn-close');
    closeButton.setAttribute('data-bs-dismiss', 'alert');
    closeButton.setAttribute('aria-label', 'Close');

    // Добавляем кнопку закрытия в alert
    newAlert.appendChild(closeButton);

    // Добавляем alert в контейнер на странице
    messageContainer.appendChild(newAlert);

    // Удаляем alert через 5 секунд
    setTimeout(() => newAlert.remove(), 5000);
}

