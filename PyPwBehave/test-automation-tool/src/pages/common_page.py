
from playwright.sync_api import sync_playwright, expect
import time
from elementsPage.general_variables import *


class OpenApplication:

   def launch_browser_and_open_page(self):
         self.playwright = sync_playwright().start()

         if browser.lower() == "chromium":
             self.browser = self.playwright.chromium.launch(headless=False)
         elif browser.lower() == "firefox":
             self.browser = self.playwright.firefox.launch(headless=False)
         elif browser.lower() == "webkit":
             self.browser = self.playwright.webkit.launch(headless=False)
         else:
             raise ValueError("Navegador inválido")

         self.page = self.browser.new_page()
         # Open login page
         self.page.goto(url_qa)
         title =  self.page.title()
         print(" >>> Título da página:", title)
         assert title == "Front - ServeRest"
         expect(self.page).to_have_title("Front - ServeRest")
         time.sleep(1)

   def login_ui(self):
        self.page.locator('//*[@id="root"]/div/div/form/small/a').wait_for(state="visible", timeout=5000)
        self.page.locator('//*[@id="root"]/div/div/form/small/a').click()
        #validate that is register page
        titulo = self.page.locator("h2").inner_text()
        print('>>>>>',titulo)
        #playwright assertion
        expect(self.page.locator("h2")).to_have_text('Cadastro')
        # self.page.pause()
        # self.page.wait_for_timeout(50000)
        #python assertion
        assert titulo == 'Cadastro'
        self.page.wait_for_timeout(5000)


