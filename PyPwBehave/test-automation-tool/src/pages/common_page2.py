from playwright.sync_api import Playwright, sync_playwright, Page, expect
from  elementsPage.general_variables import *


class Log_administrator:
    def launch_browser_and_open_page_administrator(self,browser,headless_mode):
         # with sync_playwright() as playwright:
            self.playwright = sync_playwright().start()

            if browser.lower() == "chrome":
                self.browser = self.playwright.chromium.launch(
                    headless=headless_mode,
                    channel="chrome")
            elif browser.lower() == "edge":
                self.browser = self.playwright.chromium.launch(headless=headless_mode, channel="msedge")
            elif browser.lower() == "firefox":
                self.browser = self.playwright.firefox.launch(headless=headless_mode)
            elif browser.lower() == "webkit":
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
            else:
                raise ValueError("Navegador inválido")

         # Cria contexto SEM definir viewport



            self.page = self.browser.new_page()
            # Open login page
            self.page.goto(url_qa)


    # def login_ui_administrator(self):
    #         self.page.get_by_test_id("email").wait_for(state="visible")
    #         self.page.get_by_test_id("email").fill('raul.santos@bee-eng.pt')
    #         self.page.get_by_test_id("senha").fill('JiA4ever#yj12')
    #         # self.page.pause()
    #         # self.page.wait_for_timeout(5000000)
    #         self.page.get_by_test_id("entrar").click()
    #         self.page.get_by_test_id("listar-usuarios").click()
    #         # elements = self.page.locator('//*[@id="root"]/div/div/p/table/tbody').count()
    #         self.page.locator("table tbody tr").first.wait_for()
    #         rows = self.page.locator("table tbody tr").count()
    #         print('elementos:', rows)
    #
    #         for i in range(rows):
    #             second_td = self.page.locator(f'//*[@id="root"]/div/div/p/table/tbody/tr[{i + 1}]/td[2]').inner_text()
    #             print('linhas: ',i,'email: ', second_td)
    #
    #             if second_td == 'raul.santos@bee-eng.pt':
    #               expect(self.page.locator(f'//*[@id="root"]/div/div/p/table/tbody/tr[{i + 1}]/td[2]')).to_have_text('raul.santos@bee-eng.pt')
    #               print('>>>>>>>>>>>',second_td )
    #               self.page.wait_for_timeout(2000)
    #               break
    #               ######## comentei pois ta tudo bem mas a pagina nao funiona erro da propria pagina o click button editar
    #               # button = self.page.locator(f'//*[@id="root"]/div/div/p/table/tbody/tr[{i+1}]//td[5]]/div/button[1]')
    #               # button.scroll_into_view_if_needed()
    #               # button.dblclick()









    def test_example(page: Page) -> None:
            page.get_by_test_id("email").click()
            page.get_by_test_id("email").fill("raul.santos@bee-eng.pt")
            page.get_by_test_id("senha").click()
            page.get_by_test_id("senha").fill("JiA4ever#yj12")
            page.get_by_test_id("entrar").click()
            page.get_by_test_id("listar-usuarios").click()
            page.pause()
            page.wait_for_timeout(50000)