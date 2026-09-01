from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Pagelogin:

    URL_BASE = "https://listado.mercadolibre.com.ar/mer%C3%A7ado-libre-argentina?gclsrc=aw.ds&gad_source=1&gad_campaignid=24076337197&gbraid=0AAAAAC-CuxPJR2Hqpps_3xo_l8IRiH0TD&gclid=EAIaIQobChMIkIH11KHOlgMVpFZIAB0a2DuOEAAYASAAEgKUNPD_BwE"
    EMAIL = (By.ID, "identifierId")
    PASSWORD = (By.CLASS_NAME, "whsOnd zHQkBf")
    BTN_INGRESA = (By.ID, "login")
    BTN_I_S_GOOGLE = (By.CLASS_NAME, "nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb ")
    BTN_SIGUIENTE = (By.CLASS_NAME, "VfPpkd-RLmnJb")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def open(self):
        self.driver.get(self.URL_BASE)

    def loginConGoogle(self, email, password):
        self.driver.find_element(*self.BTN_INGRESA).click()
        self.driver.find_element(*self.BTN_I_S_GOOGLE).click()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.BTN_SIGUIENTE).click()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.BTN_SIGUIENTE).click()
