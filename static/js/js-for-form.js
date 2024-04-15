document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('data-form');
    const clearBtn = document.getElementById('clear-btn');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        let valid = true;
        let errorMessage = '';

        if (!name) {
            errorMessage += 'Имя не должно быть пустым.\n';
            valid = false;
        }

        if (!email) {
            errorMessage += 'Email не должен быть пустым.\n';
            valid = false;
        } else if (!/^\S+@\S+\.\S+$/.test(email)) {
            errorMessage += 'Введите корректный Email.\n';
            valid = false;
        }

        if (valid) {
            form.submit(); // Если данные валидны, отправляем форму
        } else {
            alert(errorMessage); // Если данные невалидны, показываем ошибку
        }
    });

    // Обработчик события для кнопки "Clear"
    clearBtn.addEventListener('click', function () {
        document.getElementById('name').value = ''; // Очищаем поле ввода имени
        document.getElementById('email').value = ''; // Очищаем поле ввода email
    });
});
