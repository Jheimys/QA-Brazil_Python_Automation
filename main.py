# Tarefa 3: Importar arquivos de apoio
import data # Contém constantes como URLs, endereços e informações do cartão
import helpers # Contém funções utilitárias, como verificação do servidor

from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages import UrbanRoutesPage
class TestUrbanRoutes:
    # Tarefa 4: Verificar se o servidor Urban Routes estátou  acessível antes de rodar os testes
    @classmethod
    def setup_class(cls):

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

        # Usa função de helpers.py para verificar conectividade com o servidor
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    # Tarefa 3: Criar função para testar definição de rota
    def test_set_route(self):
        """
        Testa se, ao inserir os endereços de origem e destino, a interface exibe a opção de seleção de planos.
        O teste garante que a área de seleção de planos só aparece após o preenchimento correto dos campos
        de endereço.

        """
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        actual_value = urban_routes_page.is_plan_selection_visible()
        expected_value = True
        assert expected_value == actual_value, f"Esperado que a seleção de planos estivesse visível, mas não estava."


    # Tarefa 3: Criar função para testar seleção de plano
    def test_select_plan(self):
        """
        Testa se, após selecionar o plano, o botão 'Comfort' foi clicado e seu texto corresponde ao esperado.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        actual_value = urban_routes_page.get_comfort_button_text()
        expected_value = "Comfort"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"


    # Tarefa 3: Criar função para testar preenchimento do número de telefone
    def test_fill_phone_number(self):
        """
          Testa se, após preencher e confirmar o número de telefone, o campo de input exibe o valor correto.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        actual_value = urban_routes_page.get_phone_number_value()
        expected_value = data.PHONE_NUMBER
        assert expected_value == actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"


    # Tarefa 3: Criar função para testar preenchimento dos dados do cartão
    def test_fill_card(self):
        """
          Testa se, após preencher os dados do cartão, a opção 'Cartão' aparece como método de
          pagamento selecionado.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)

        actual_value = urban_routes_page.is_card_selected()
        expected_value = True
        assert expected_value == actual_value, ("Esperado que a opção 'Cartão' estivesse selecionada após o "
                                                "preenchimento dos dados.")

    # Tarefa 3: Criar função para testar comentário para o motorista
    def test_comment_for_driver(self):
        """
            Testa se, após preencher a mensagem para o motorista, o campo de input exibe o valor correto.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)

        actual_value = urban_routes_page.get_driver_message()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert expected_value == actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"

    # Tarefa 3: Criar função para testar pedido de cobertor e lenços
    def test_order_blanket_and_handkerchiefs(self):
        """
          Testa se, após solicitar cobertor e lençóis, o checkbox correspondente está marcado.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.order_blanket_and_handkerchiefs()

        actual_value = urban_routes_page.is_blanket_checkbox_checked()
        expected_value = True
        assert expected_value == actual_value, ("Esperado que o checkbox de cobertor e lençóis estivesse marcado, "
                                                "mas não estava.")

    # Tarefa 5: Criar função com loop para testar pedido de 2 sorvetes
    def test_order_2_ice_creams(self):
        """
            Testa se, após pedir sorvete, a quantidade exibida no contador é igual a 2.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.order_ice_cream()

        actual_value = urban_routes_page.get_ice_cream_quantity()
        expected_value = 2
        assert expected_value == actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"

    # Tarefa 3: Criar função para testar se o modelo de carro aparece na busca
    def test_car_search_model_appears(self):
        """
        Testa se, após pedir o táxi e aguardar o processo de busca, o modelo do carro aparece na interface.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        urban_routes_page.select_plan()
        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_blanket_and_handkerchiefs()
        urban_routes_page.order_ice_cream()
        urban_routes_page.final_steps()
        urban_routes_page.wait_for_search_popup_to_disappear()

        actual_value = urban_routes_page.get_car_model_number()
        assert actual_value.strip() != "", f"Esperado que o modelo do carro aparecesse, mas recebeu '{actual_value}'"

    def test_final_steps(self):
        """
           Testa se, após todas as etapas e clicar em 'Pedir', o popup mostra o título correto indicando
           o tempo de Buscar carro.
        """

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)

        urban_routes_page.order_blanket_and_handkerchiefs()

        urban_routes_page.order_ice_cream()

        urban_routes_page.final_steps()

        actual_value = urban_routes_page.get_order_popup_title()
        expected_value = "Buscar carro"
        assert expected_value in actual_value, f"Esperado '{expected_value}', mas recebeu '{actual_value}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()