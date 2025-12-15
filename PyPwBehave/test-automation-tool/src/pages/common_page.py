
from playwright.sync_api import sync_playwright, expect
import time
from  elementsPage.general_variables import *


class OpenApplication:

   def launch_browser_and_open_page(self,browser):
         self.playwright = sync_playwright().start()

         if browser.lower() == "chrome":
             self.browser = self.playwright.chromium.launch(headless=True, channel="chrome")
         elif browser.lower() == "edge":
             self.browser = self.playwright.chromium.launch(headless=True, channel="msedge")
         elif browser.lower() == "firefox":
             self.browser = self.playwright.firefox.launch(headless=True)
         elif browser.lower() == "webkit":
             self.browser = self.playwright.webkit.launch(headless=True)
         else:
             raise ValueError("Navegador inválido")

         self.page = self.browser.new_page()
         # Open login page
         self.page.goto(url_qa)
         title =  self.page.title()
         assert title == "Front - ServeRest"
         expect(self.page).to_have_title("Front - ServeRest")
         print(" >>> Título da página:", title)

   def login_ui(self):
        self.page.get_by_test_id("email").wait_for(state="visible", timeout=5000)
        self.page.get_by_test_id("email").fill('rsraulsnts@gmail.com')
        self.page.get_by_test_id("senha").fill('JiA4ever#yj12')
        # self.page.pause()
        # self.page.wait_for_timeout(5000000)
        self.page.get_by_test_id("entrar").click()
        #self.page.get_by_role("heading", name="Bem Vindo Raul Santos").wait_for(state="visible")
        self.page.get_by_role("heading",name="Serverest Store").wait_for(state="visible")

   def validate_client_area_page(self):
       #text =  self.page.get_by_role("heading", name="Bem Vindo Raul Santos").inner_text()
       text = self.page.get_by_role("heading",name="Serverest Store").inner_text()
       # assert text == "Bem Vindo Raul Santos"
       assert text == "Serverest Store"
       print("assert validation pass----" ,text)
       self.page.wait_for_timeout(5000)






