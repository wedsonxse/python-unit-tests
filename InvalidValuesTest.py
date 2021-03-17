from selenium import webdriver
import time
import unittest

#Este teste avalia se o formulário está realizando o tratamento necessário para os casos
#onde algum dos campos contêm valores inválidos

class InvalidValuesTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def test_invalid_values(self):
        self.driver = self.browser
        self.driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")

        #Localiza e envia um valor inválido ao campo de nome
        UserName = self.driver.find_element_by_css_selector(".col-md-7 .ddm-field-text")
        UserName.send_keys('$$$')

        time.sleep(1)

        #Localiza e envia um valor inválido ao campo de motivação
        WhyDidYouJoin = self.driver.find_element_by_css_selector(".col-md-12 > .form-group > .ddm-field-text")
        WhyDidYouJoin.send_keys('$$$$')

        time.sleep(1)

        #Localiza e define uma data de aniversário padrão
        BirthDate = self.driver.find_element_by_css_selector(".lexicon-icon-calendar")
        BirthDate.click()

        time.sleep(1)

        BirthDay = self.driver.find_element_by_css_selector(".rowgroup:nth-child(1) > .day:nth-child(4)")
        BirthDay.click()

        time.sleep(1)

        #clica no botão de submit
        Submit = self.driver.find_element_by_css_selector(".btn-primary")
        Submit.click()

        #aguarda um período curto para garantir o envio
        time.sleep(2)

        #Testa se a mensagem de sucesso não está presente na página de resposta
        assert "Information sent successfully!" not in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()