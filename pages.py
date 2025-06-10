from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    # Localizadores
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    COMFORT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(), "Comfort")]')
    INPUT_PHONE = (By.XPATH, '//div[@class="np-text" and contains(text(), "Número de telefone")]')
    PHONE_NUMBER = (By.ID, 'phone')
    BTN_NEXT = (By.XPATH, '//button[@class="button full"]')
    CODE_INPUT = (By.ID, 'code')
    BTN_CONFIRM = (By.XPATH, '//button[@class="button full" and contains(text(),"Confirmar")]')

    # 🆕 localizadores para o cartão
    INPUT_CARD = (By.XPATH, '//div[@class="pp-button filled"]')
    ADD_CARD = (By.XPATH,'//div[@class="pp-row disabled"]')
    ADD_CARD_NUMBER = (By.ID, 'number')
    ADD_CARD_CODE = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    CLICK_CARD_TITlE = (By.XPATH, '//div[@class="head" and contains(text(),"Adicionar um cartão" )]')
    BTN_CARD_ADD = (By.XPATH,'//button[@class="button full" and contains(text(),"Adicionar" )]')
    BTN_CLOSE_CARD = (By.CSS_SELECTOR, '.payment-picker.open .close-button.section-close')

    # 🆕 Mensagem para o motorista
    INPUT_DRIVER_MESSAGE = (By.ID, 'comment')

    # 🆕 Pedidos ao  motorista
    ORDER_DRIVER = (By.XPATH, '//div[contains(@class, "reqs")]')
    #CHECKBOX_INPUT = (By.XPATH, '//input[@type="checkbox" and @wfd-id="id8"]')
    CHECKBOX_INPUT = (
        By.XPATH,
        '//div[@class="r-sw-label" and contains(text(), "Cobertor e lençóis")]'
        '/following-sibling::div//input[@type="checkbox"]'
    )

    CHECKBOX_VISUAL = (
        By.XPATH,
        '//div[@class="r-sw-label" and contains(text(), "Cobertor e lençóis")]'
    )

    ICE_CREAM_BUTTON = (By.XPATH,'//div[contains(@class, "option") and contains(text(), "Sorvete")]')

    def __init__(self, driver):
        self.driver = driver

    # Localizações
    def enter_from_location(self, from_text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FROM_LOCATOR)
        ).send_keys(from_text)

    def enter_to_location(self, to_text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TO_LOCATOR)
        ).send_keys(to_text)

    def click_book_button(self):
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def select_comfort(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMFORT_BUTTON_LOCATOR)
        )
        if "active" not in comfort_button.get_attribute("class"):
            comfort_button.click()

    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

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

    def comment_for_driver(self, message):
        self.write_driver_message(message)

    #------ Pedidos cobertor ---------------------
    # def order_driver(self):
    #     order_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.ORDER_DRIVER)
    #     )
    #     if "open" not in order_button.get_attribute("class"):
    #         order_button.click()

    # def checkbox_blanket(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.CHECKBOX_INPUT)
    #     ).click()

    def order_driver(self):
        order_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ORDER_DRIVER)
        )

        if "open" not in order_section.get_attribute("class"):
            order_section.click()
            # Espera até que a classe 'open' esteja presente
            WebDriverWait(self.driver, 5).until(
                lambda d: "open" in d.find_element(*self.ORDER_DRIVER).get_attribute("class")
            )

    # def checkbox_blanket(self):
    #     try:
    #         visual_checkbox = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(self.CHECKBOX_VISUAL)
    #         )
    #         print("🟢 Checkbox visual localizado e clicável.")
    #
    #         self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    #                                    visual_checkbox)
    #         import time
    #         time.sleep(1)  # para garantir scroll
    #
    #         print("⏸️ Pausando 2 segundos antes de clicar...")
    #         time.sleep(2)
    #
    #         self.driver.execute_script("arguments[0].click();", visual_checkbox)
    #
    #         print("✅ Checkbox clicado com sucesso.")
    #
    #         # 🔎 Pausa para ver depois do clique
    #         print("⏸️ Pausando 2 segundos após o clique...")
    #         time.sleep(2)
    #     except Exception as e:
    #         print("❌ Erro ao clicar no visual do checkbox:", str(e))

    def checkbox_blanket(self):
        try:
            checkbox_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CHECKBOX_INPUT)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       checkbox_input)

            import time
            time.sleep(2)

            # Marca o checkbox diretamente
            self.driver.execute_script("arguments[0].checked = true;", checkbox_input)

            # Dispara evento de mudança, se necessário
            self.driver.execute_script("""
                let event = new Event('change', { bubbles: true });
                arguments[0].dispatchEvent(event);
            """, checkbox_input)

            time.sleep(1)

            # Verifica se foi marcado
            is_checked = self.driver.execute_script("return arguments[0].checked;", checkbox_input)
            print(f"✅ Checkbox marcado? {is_checked}")

        except Exception as e:
            print("❌ Erro ao forçar marcação do checkbox:", str(e))

    def order_blanket_and_handkerchiefs(self):
        self.order_driver()
        self.checkbox_blanket()

    # def select_blanket(self):
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.BLANKET_CHECKBOX)
    #     ).click()

    def order_ice_cream(self, quantity=2):
        for _ in range(quantity):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ICE_CREAM_BUTTON)
            ).click()

    def final_steps(self, message="Olá motorista!", ice_cream_qty=2):
        self.write_driver_message(message)
        self.select_blanket()
        self.order_ice_cream(ice_cream_qty)



