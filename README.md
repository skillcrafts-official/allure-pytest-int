## Шпаргалка по pytest и allure (интеграция)
### 1. Установка и подготовка
```bash
pip install pytest allure-pytest
```

### 2. Структура тестового файла `test_demo.py`
```python
import allure
import pytest

@allure.feature("Авторизация")
@allure.story("Успешный вход")
def test_successful_login():
    with allure.step("Шаг 1: открыть страницу логина"):
        pass
    with allure.step("Шаг 2: ввести логин и пароль"):
        login, password = "user", "pass"
        allure.attach("логин: user", name="credentials", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Шаг 3: нажать кнопку Войти"):
        pass
    with allure.step("Шаг 4: проверить переход на главную"):
        assert True

@allure.feature("Авторизация")
@allure.story("Неверный пароль")
def test_failed_login():
    with allure.step("Ввести неправильный пароль"):
        assert False, "Ожидалась ошибка"
```
### 3. Запуск тестов с сохранением результатов
```bash
pytest --alluredir=./allure-results test_demo.py
```
В папке `allure-results` появятся JSON-файлы с результатами.

### 4. Отправка отчёта в Allure Docker Service (порт 5050)
#### Ошибка: `{"meta_data":{"message":"'files[]' array is empty"}}`
Причина: неверное имя поля формы. Сервер ожидает `files[]`, а не `allureResults`.
В зависимости от версии allure (в этой шпаргалке используется docker-allure).
Ошибка возникает, если сделать curl отправку с неверным ключом (не files[]), ничего не отобразиться в allure, 
если отправить zip-архив.

#### Исправление (каждый файл отдельно):
```bash
args=()
for file in allure-results/*; do
  if [ -f "$file" ]; then
    args+=(-F "files[]=@$file")
  fi
done
curl -X POST "http://127.0.0.1:5050/allure-docker-service/send-results?project_id=default" "${args[@]}"
```
После успешной отправки сервер вернёт `{"status":"success"}`, и отчёт станет доступен по адресу:
```text
http://127.0.0.1:5050/allure-docker-service/projects/default/reports/latest/index.html?redirect=false
```


