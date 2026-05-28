import allure
import pytest

@allure.feature("Авторизация")
@allure.story("Успешный вход")
def test_successful_login():
    with allure.step("Шаг 1: открыть страницу логина"):
        # здесь мог бы быть Selenium/requests
        pass
    with allure.step("Шаг 2: ввести логин и пароль"):
        login, password = "user", "pass"
        allure.attach("логин: user", name="credentials", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Шаг 3: нажать кнопку Войти"):
        pass
    with allure.step("Шаг 4: проверить переход на главную"):
        assert True  # замени настоящей проверкой

@allure.feature("Авторизация")
@allure.story("Неверный пароль")
def test_failed_login():
    with allure.step("Ввести неправильный пароль"):
        assert False, "Ожидалась ошибка"