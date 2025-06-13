from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import data


class UrbanRoutesPage:
    # Localizadores campo from e to
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    PLAN_SELECTION_LOCATOR = (By.XPATH, '//div[@class="type-picker shown"]')

    #Localizadores
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    COMFORT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(), "Comfort")]')

    # Localizadores de telefone
    INPUT_PHONE = (By.XPATH, '//div[@class="np-text" and contains(text(), "Número de telefone")]')
    PHONE_NUMBER = (By.ID, 'phone')
    BTN_NEXT = (By.XPATH, '//button[@class="button full"]')
    CODE_INPUT = (By.ID, 'code')
    BTN_CONFIRM = (By.XPATH, '//button[@class="button full" and contains(text(),"Confirmar")]')

    # localizadores para o cartão
    INPUT_CARD = (By.XPATH, '//div[@class="pp-button filled"]')
    ADD_CARD = (By.XPATH,'//div[@class="pp-row disabled"]')
    ADD_CARD_NUMBER = (By.ID, 'number')
    ADD_CARD_CODE = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    CLICK_CARD_TITlE = (By.XPATH, '//div[@class="head" and contains(text(),"Adicionar um cartão" )]')
    BTN_CARD_ADD = (By.XPATH,'//button[@class="button full" and contains(text(),"Adicionar" )]')
    BTN_CLOSE_CARD = (By.CSS_SELECTOR, '.payment-picker.open .close-button.section-close')
    CARD_SELECTED_TEXT = (By.XPATH, '//div[@class="pp-value-text" and text()="Cartão"]')

    # Mensagem para o motorista
    INPUT_DRIVER_MESSAGE = (By.ID, 'comment')

    # Pedidos ao  motorista
    ORDER_DRIVER = (By.XPATH, '//div[contains(@class, "reqs")]')
    CHECKBOX_INPUT = (
        By.XPATH,
        '//div[@class="r-sw-label" and contains(text(), "Cobertor e lençóis")]'
        '/following-sibling::div//input[@type="checkbox"]'
    )

    CHECKBOX_VISUAL = (
        By.XPATH,
        '//div[@class="r-sw-label" and contains(text(), "Cobertor e lençóis")]'
    )

    # Pedidir 2 sorvetes
    ICE_CREAM_BUTTON = (
        By.XPATH,
        '//div[@class="r-counter-label" and text()="Sorvete"]/following-sibling::div'
        '//div[contains(@class,"counter-plus")]'
    )

    ICE_CREAM_COUNTER_VALUE = (By.XPATH, '//div[@class="counter-value"]')

    # Pedir taxi
    BTN_ASK = (By.XPATH, '//button[@class="smart-button"]//span[text()="Pedir"]')
    ORDER_HEADER_TITLE = (By.XPATH, '//div[contains(@class,"order-header-title") and text()="Buscar carro"]')
    CAR_MODEL_NUMBER = (By.XPATH, '//div[@class="number"]')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, address_from, address_to):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.driver.implicitly_wait(3)
        self.enter_locations(address_from, address_to)


    # Localizações dos campo from e to
    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FROM_LOCATOR)
        ).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TO_LOCATOR)
        ).send_keys(to_text)

    def is_plan_selection_visible(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.PLAN_SELECTION_LOCATOR)
            )
            return element.is_displayed()
        except:
            return False

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    # ---- Selecionar a opção Confort
    def click_book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def select_comfort(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMFORT_BUTTON_LOCATOR)
        )
        if "active" not in comfort_button.get_attribute("class"):
            comfort_button.click()

    def get_comfort_button_text(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMFORT_BUTTON_LOCATOR)
        )
        return comfort_button.text

    def select_plan(self):
        self.click_book_button()
        self.select_comfort()

    # -------- Telefone ----------------------
    def click_input_phone(self):
        self.driver.find_element(*self.INPUT_PHONE).click()

    def enter_phone_number(self, number_phone):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PHONE_NUMBER)
        ).send_keys(number_phone)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BTN_NEXT)
        ).click()

    def wait_for_code_input(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CODE_INPUT)
        )

    def get_sms_code(self):
        import helpers
        return helpers.retrieve_phone_code(self.driver)

    def enter_sms_code(self, code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CODE_INPUT)
        ).send_keys(code)

    def click_btn_confirm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BTN_CONFIRM)
        ).click()

    def get_phone_number_value(self):
        input_field = self.driver.find_element(*self.PHONE_NUMBER)
        return input_field.get_attribute("value")

    def fill_phone_number(self, number_phone):
        self.click_input_phone()
        self.enter_phone_number(number_phone)
        self.click_next_button()
        self.wait_for_code_input()
        sms_code = self.get_sms_code()
        self.enter_sms_code(sms_code)
        self.click_btn_confirm()

    #--------- Cartão --------------------------------
    def enter_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_CARD)
        ).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD)
        ).click()

    def add_card_number(self, number):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD_NUMBER)
        ).send_keys(number)

    def add_card_code(self, code_number):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_CARD_CODE)
        ).send_keys(code_number)

    def click_card_title(self):
        self.driver.find_element(*self.CLICK_CARD_TITlE).click()

    def click_card_btn_add(self):
        self.driver.find_element(*self.BTN_CARD_ADD).click()

    def click_close_card(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BTN_CLOSE_CARD)
        ).click()

    def is_card_selected(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.CARD_SELECTED_TEXT)
            )
            return element.is_displayed()
        except:
            return False

    def fill_card(self, number, code_number):
        self.enter_card()
        self.click_add_card()
        self.add_card_number(number)
        self.add_card_code(code_number)
        self.click_card_title()
        self.click_card_btn_add()
        self.click_close_card()

    # ------ Mensagem  ----------------------------
    def write_driver_message(self, message):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INPUT_DRIVER_MESSAGE)
        ).send_keys(message)

    def get_driver_message(self):
        input_field = self.driver.find_element(*self.INPUT_DRIVER_MESSAGE)
        return input_field.get_attribute("value")

    def comment_for_driver(self, message):
        self.write_driver_message(message)

    #------ Pedidos cobertor ---------------------
    def order_driver(self):
        # Aguarda todos os elementos visuais de checkbox (ex: r-sw-label) estarem presentes
        checkbox_visuals = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CHECKBOX_VISUAL)
        )
        # Clica na primeira opção visual (assumindo que é o cobertor)
        checkbox_visuals[0].click()

    def checkbox_blanket(self):
        try:
            checkbox_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CHECKBOX_INPUT)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       checkbox_input)

            #time.sleep(2)

            # Marca o checkbox diretamente
            self.driver.execute_script("arguments[0].checked = true;", checkbox_input)

            # Dispara evento de mudança, se necessário
            self.driver.execute_script("""
                let event = new Event('change', { bubbles: true });
                arguments[0].dispatchEvent(event);
            """, checkbox_input)

            #time.sleep(1)

            # Verifica se foi marcado
            is_checked = self.driver.execute_script("return arguments[0].checked;", checkbox_input)
            print(f"✅ Checkbox marcado? {is_checked}")

        except Exception as e:
            print("❌ Erro ao forçar marcação do checkbox:", str(e))

    # ---- vesão mais simples apresenta bugs ---------------------
    # def checkbox_blanket(self):
    #     # Aguarda todos os checkboxes do tipo input[type="checkbox"]
    #     checkboxes = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]'))
    #     )
    #     # Retorna se o primeiro checkbox está marcado
    #     return checkboxes[0].is_selected()

    def is_blanket_checkbox_checked(self):
        checkbox_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CHECKBOX_INPUT)
        )
        return self.driver.execute_script("return arguments[0].checked;", checkbox_input)

    def order_blanket_and_handkerchiefs(self):
        self.order_driver()
        self.checkbox_blanket()


#------ Pedir 2 sorvetes ---------------------------------------
    def order_ice_cream(self, quantity=2):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ICE_CREAM_BUTTON)
        )
        for _ in range(quantity):
            button.click()
            #time.sleep(1)

    def get_ice_cream_quantity(self):
        counter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ICE_CREAM_COUNTER_VALUE)
        )
        return int(counter.text)

    def order_2_ice_creams(self):
        self.order_driver()
        self.order_ice_cream()

#------------- Pedir taxi ------------------------
    def get_car_model_number(self, timeout=60):
        # Aguarda até o elemento do modelo do carro aparecer após o fechamento do popup anterior
        car_model_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.CAR_MODEL_NUMBER)
        )
        return car_model_element.text

    def wait_for_search_popup_to_disappear(self, timeout=45):
        WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(
                self.ORDER_HEADER_TITLE, "Buscar carro"
            )
        )

    def btn_ask(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BTN_ASK)
        ).click()
        time.sleep(2)

    def get_order_popup_title(self):
        title_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ORDER_HEADER_TITLE)
        )
        return title_element.text

    def final_steps(self):
        self.btn_ask()




