import pytest
from Object.object_ui import Object_ui
import allure


@allure.title("Проверка поля 'Когда'")
@allure.description(" Поле 'Когда' обязательно к заполнению")
@allure.feature("READ")
@allure.severity("critical")
def test_no_date(driver):

    object_ui = Object_ui(driver)
    with allure.step("Принимаем куки"):
        object_ui.accept_cookie()
    with allure.step("Заполняем поля 'Куда'"):
        object_ui.set_input_place("Москва")
    with allure.step("Заполняем поля 'Откуда'"):
        object_ui.set_output_place()
    with allure.step("Нажимаем 'Найти билеты'"):
        object_ui.push_button()

    with allure.step("Проверяем появление планки с сообщением об ошибке"):
        assert object_ui.get_bar() == "УКАЖИТЕ ДАТУ"


@allure.title("Проверка поля 'Откуда'")
@allure.description(" Поле 'Откуда' обязательно к заполнению")
@allure.feature("READ")
@allure.severity("critical")
def test_no_input_place(driver):
    object_ui = Object_ui(driver)
    with allure.step("Принимаем куки"):
        object_ui.accept_cookie()
    with allure.step("Заполняем поля 'Откуда'"):
        object_ui.set_output_place("Новосибирск")
    with allure.step("Заполняем поля 'Когда'"):
        object_ui.set_data("22.04.2025")
    with allure.step("Нажимаем 'Найти билеты'"):
        object_ui.push_button()

    with allure.step("Проверяем появление планки с сообщением об ошибке"):
        assert object_ui.get_bar() == "УКАЖИТЕ ГОРОД ПРИБЫТИЯ"


@allure.title("Проверка всплывающего окна в поле 'Откуда' ")
@allure.description("При заполнении поля 'Откуда' появляется всплывающее окно с возможными вариантами")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.parametrize(
    'creds',
    [
        '...Москва',
        '-Москва',
        'Moscow'
    ]
)
def test_name_input_city(driver, creds):
    city = creds
    object_ui = Object_ui(driver)
    with allure.step("Принимаем куки"):
        object_ui.accept_cookie()
    with allure.step("Заполняем поля 'Куда'"):
        object_ui.set_input_place(city)


    with allure.step("Проверяем появление всплывающего окна и автовыбор первого результата"):
        assert object_ui.get_city_name("destination") == "Москва"


@allure.title("Проверка всплывающего окна в поле 'Куда' ")
@allure.description("При заполнении поля 'Куда' появляется всплывающее окно с возможными вариантами")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.parametrize(
    'creds',
    [
        '...Новосибирск',
        '-Новосибирск',
        'Novosib'
    ]
)
def test_name_output_city(driver, creds):
    city = creds
    object_ui = Object_ui(driver)
    with allure.step("Принимаем куки"):
        object_ui.accept_cookie()
    with allure.step("Заполняем поля 'Откуда'"):
        object_ui.set_output_place(city)


    with allure.step("Проверяем появление всплывающего окна и автовыбор первого результата"):
        assert object_ui.get_city_name("origin") == "Новосибирск"

@allure.title("Проверка кнопки 'Найти билеты'")
@allure.description("Возвращает количество доступных билетов")
@allure.feature("READ")
@allure.severity("critical")
def test_price(driver):
        object_ui = Object_ui(driver)
        object_ui.accept_cookie()
        object_ui.set_output_place("Новосибирск")
        object_ui.set_input_place("Москва")
        object_ui.set_data("25.04.2025")
        object_ui.push_button()

        with allure.step("Проверяем появление планки с сообщением об ошибке"):
            assert object_ui.get_price() > 0
