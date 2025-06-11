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
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')

    # Tarefa 3: Criar função para testar seleção de plano
    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()


    # Tarefa 3: Criar função para testar preenchimento do número de telefone
    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)


    # Tarefa 3: Criar função para testar preenchimento dos dados do cartão
    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        # urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)

    # Tarefa 3: Criar função para testar comentário para o motorista
    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)

    # Tarefa 3: Criar função para testar pedido de cobertor e lenços
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.order_blanket_and_handkerchiefs()

    # Tarefa 5: Criar função com loop para testar pedido de 2 sorvetes
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.order_ice_cream()

    # Tarefa 3: Criar função para testar se o modelo de carro aparece na busca
    # def test_car_search_model_appears(self):
    #     # Adicionar em S8
    #     print("função criada para verificar se o modelo do carro aparece na busca")
    #     pass

    def test_final_steps(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)

        self.driver.implicitly_wait(3)

        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        urban_routes_page.select_plan()

        urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        urban_routes_page.comment_for_driver(data.MESSAGE_FOR_DRIVER)

        urban_routes_page.order_blanket_and_handkerchiefs()

        urban_routes_page.order_ice_cream()

        urban_routes_page.final_steps()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()