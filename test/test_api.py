import requests
import allure


base_url = "https://min-prices.aviasales.ru/"
my_headers = {"Cookie": "nuid=6e9a1628-9439-4d92-a6f6-8dbee088ba86",
              "Content-Type": "application/json"}

@allure.title("Проверка стоимости билета первого варианта")
@allure.feature("READ")
@allure.severity("critical")
def test_get_price():
    resp = requests.get(base_url+'price_matrix?origin_iata=LED&destination_iata=UFA&depart_start=2025-04-15&depart_range=6&affiliate=false&market=ru').json()

    with allure.step("Проверяем, что стоимость билета первого варианта больше 0"):
        assert(resp["prices"][0]["value"])>1000

@allure.title("Проверка перелета по городам России")
@allure.feature("READ")
@allure.severity("critical")
def test_rus_city():
    resp = requests.get(base_url+'price_matrix?origin_iata=LED&destination_iata=UFA&depart_start=2025-04-15&depart_range=6&affiliate=false&market=ru')

    with allure.step("Проверяем успешность выполнения запроса"):
        assert resp.status_code == 200

@allure.title("Проверка перелета по городам зарубежья")
@allure.feature("READ")
@allure.severity("critical")
def test_foreign_city():
    resp = requests.get(base_url+'price_matrix?origin_iata=LED&destination_iata=NQZ&depart_start=2025-04-15&depart_range=6&affiliate=false&market=ru')

    with allure.step("Проверяем успешность выполнения запроса"):
        assert resp.status_code == 200

@allure.title("Проверка возможности просмотра стоимости билетов за прошедшую неделю")
@allure.feature("READ")
@allure.severity("normal")
def test_get_data_last_week():
    resp = requests.get(base_url+'price_matrix?origin_iata=LED&destination_iata=UFA&depart_start=2025-04-10&depart_range=6&affiliate=false&market=ru').json()

    with allure.step("Проверяем, что вернулся ненулевой список"):
        assert len(resp["prices"]) > 0

@allure.title("Проверка поиска билетов без даты отправления")
@allure.feature("READ")
@allure.severity("critical")
def test_no_data():
    resp = requests.get(base_url+'price_matrix?origin_iata=LED&destination_iata=UFA&depart_range=6&affiliate=false&market=ru')

    with allure.step("Проверяем успешность запроса"):
        assert resp.status_code == 400
