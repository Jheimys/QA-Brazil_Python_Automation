# Tarefa 3: Importar arquivos de apoio
import data # Contém constantes como URLs, endereços e informações do cartão
import helpers # Contém funções utilitárias, como verificação do servidor

class TestUrbanRoutes:
    # Tarefa 4: Verificar se o servidor Urban Routes está acessível antes de rodar os testes
    @classmethod
    def setup_class(cls):
        # Usa função de helpers.py para verificar conectividade com o servidor
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    # Tarefa 3: Criar função para testar definição de rota
    def test_set_route(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    # Tarefa 3: Criar função para testar seleção de plano
    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para selecionar o plano")
        pass

    # Tarefa 3: Criar função para testar preenchimento do número de telefone
    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para preencher o número de telefone")
        pass

    # Tarefa 3: Criar função para testar preenchimento dos dados do cartão
    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para preencher os dados do cartão")
        pass

    # Tarefa 3: Criar função para testar comentário para o motorista
    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para adicionar um comentário para o motorista")
        pass

    # Tarefa 3: Criar função para testar pedido de cobertor e lenços
    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para pedir cobertor e lenços")
        pass

    # Tarefa 5: Criar função com loop para testar pedido de 2 sorvetes
    def test_order_2_ice_creams(self):
        # Adicionar em S8
        print("função criada para pedir 2 sorvetes")
        pass

    # Tarefa 3: Criar função para testar se o modelo de carro aparece na busca
    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para verificar se o modelo do carro aparece na busca")
        pass