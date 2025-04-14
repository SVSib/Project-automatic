from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class Object_ui:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get("https://www.aviasales.ru/")
        self._driver.delete_cookie("set_output_place")

    def accept_cookie(self):
        """
                Принятие куки
        """

        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR,
             ".s__dqLrjmV81lbY2ctpQQWt.s__WErm7_CLb_ylgTog3lrX.s__OWNGeBF_djpi7qoBOxk4.s__f1UsosWbVEKg57lLhkEC.s__APnaNcWCoOk3iSROpftR.s__OqVcdrKHgYj98kqcUh6G"))).click()
        # self._driver.find_element(By.CSS_SELECTOR,
        #                     ".s__dqLrjmV81lbY2ctpQQWt.s__WErm7_CLb_ylgTog3lrX.s__OWNGeBF_djpi7qoBOxk4.s__f1UsosWbVEKg57lLhkEC.s__APnaNcWCoOk3iSROpftR.s__OqVcdrKHgYj98kqcUh6G").click()

    def set_input_place(self, city="Астрахань"):
        """
                Ввод места прибытия
        """

        destination = self._driver.find_element(By.CSS_SELECTOR, "#avia_form_destination-input")
        destination.send_keys(city)
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//li[@id='avia_form_destination-item-0']//div[@class='s__PFpXoB8Er78MFmktO032']"))).click()  # ожидание начала анимации загрузки

    def set_output_place(self, city="Волгоград"):
        """
                Ввод места отправления
        """
        origin = self._driver.find_element(By.CSS_SELECTOR, "#avia_form_origin-input")
        origin.clear()
        origin.send_keys(city)
        WebDriverWait(self._driver, 5, 0.1).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".s__hozqdl8_u1owv7f58Vov.s__HLWgkBC9TdsHSs4C7GgX.s__gDc4YpDycxEWC7xpbnPU.s__DoMPFi0pOpdxJqqqv6_1")))
        WebDriverWait(self._driver, 20, 0.1).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//li[@id='avia_form_origin-item-0']//div[@class='s__PFpXoB8Er78MFmktO032']"))).click()

    def set_data(self, day):
        """
        Указать дату отправления
        """
        cal = self._driver.find_element(By.CSS_SELECTOR, ".s__baueeRnAUu_J55n12MRS.s__CD4LiXCcZBHrt3JgeEqI.s__QOH8_RMDyCm4BxeyrqOt")
        cal.click()
        self._driver.implicitly_wait(5)
        data = self._driver.find_element(By.CSS_SELECTOR, f"[data-test-id='date-{day}']")
        data.click()

    def push_button(self):
        """
                Нажатие кнопки 'Найти билеты'
        """

        self._driver.find_element(By.XPATH, "//label[@class='s__KZopnM6BdOrBq2wxllIO s__uNQ9bCegGvzIxUF_Ll6p s__qVjvD0v8qX6k8PE2wIU3 root']").click()
        self._driver.find_element(By.CSS_SELECTOR, ".s__Yzjov8gtTIwlOo3oK8L3").click()

    def get_bar(self):
        """
                Ожидание планки обязательного поля
        """
        bar = WebDriverWait(self._driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".s__jLthuOOSZixeExVBMy_w.s__XKZOSKNzU20ugFQrJnJ_.s__mKolDTwVaUL0fYyF_xuI"))).text
        return bar

    def get_city_name(self, place):
        """
                Получение названия города
        """
        res = self._driver.find_element(By.CSS_SELECTOR, f"#avia_form_{place}-input").get_attribute("Value")
        return res

    def get_price(self):
        """
                        Получение количества билетов
                """
        WebDriverWait(self._driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='s__Du6HerizwCfzUru9OzfM']")))
        price = len(self._driver.find_elements(By.CLASS_NAME,
                                               "s__Zf6bXqOZBpVtdD9ja_KQ"))
        return price
