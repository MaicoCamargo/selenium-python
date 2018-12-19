import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumChrome:
    def __init__(self, driver_navegador,url):
        self.aplication = webdriver.Chrome(executable_path=driver_navegador)
        self.aplication.maximize_window()
        self.aplication.get(url)

    def login(self, email, password):

        try:
            assert 'Jornal' in self.aplication.title
        except AssertionError:
            self.aplication.quit()
            return False
        self.aplication.find_element_by_id('email').send_keys(email)
        self.aplication.find_element_by_id('senha').send_keys(password)
        self.aplication.find_element_by_id('load').submit()
        time.sleep(3)

        try:
            if not self.aplication.find_element_by_id('load'):
                print('loguei !')
                return False
            else:
                print('erro no login')
                return True
        except Exception:
            return True

    def click_menu_lateral(self, op):
        botao = self.aplication.find_element_by_partial_link_text(op)
        if botao:
            botao.click()
            print('tem:' + op)
            return True
        else:
            print('não tem:' + op)
            return False

    def cadastrar_empresa(self):
        inputs = self.aplication.find_elements_by_class_name('form-control')
        inputs[1].send_keys('07400521000185')
        time.sleep(3)
        # inputs[2].send_keys('selenium')
        inputs[3].send_keys('projeto Urmob')

        inputs[6].send_keys('97010031')
        # inputs[7].send_keys('RS')
        # inputs[8].send_keys('Cidade')
        # inputs[9].send_keys('Rua dos andradas')
        # inputs[10].send_keys('Bonfim')
        inputs[11].send_keys('Ap - 209')
        inputs[12].send_keys('1235')
        inputs[13].send_keys('Lucas')
        inputs[14].send_keys('roratto@email')
        inputs[15].send_keys('09845623410')

        inputs[4].clear()
        inputs[4].send_keys('55999299824')
        inputs[5].send_keys('55433299824')
        self.click_menu_lateral('Cadastrar Empresa')
        self.aplication.find_element_by_class_name('btn-outline-success').click()