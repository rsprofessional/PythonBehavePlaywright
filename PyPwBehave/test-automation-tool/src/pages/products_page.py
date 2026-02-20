
from playwright.sync_api import  Page, expect
from pathlib import Path
from pages.excel_page import ReadExcelDinamicaly

read_products = ReadExcelDinamicaly()

BASE_DIR = Path(__file__).resolve().parents[1]  # ajusta conforme sua estrutura
IMAGE_PATH = BASE_DIR / "files" / "product_serverrest.png"

class Products:
    
    def __init__(self, page: Page):
        self.page = page

    def register_product(self):
        products  = read_products.read_dinamicaly_products()
        print(products)
        print('to registering a product')
        self.page.get_by_test_id("cadastrar-produtos").click()
        

        for product in products:
            nome = product[0]           # product_demo_playwright5
            preco = product[1]          # 10
            descricao = product[2]      # texto
            quantidade = product[3]     # 1
            foto = product[4]          # no

            self.page.get_by_test_id("nome").fill(str(nome))
            print("produto registado:", nome)
            self.page.get_by_test_id("preco").fill(str(preco))
            print("produto registado:", preco)
            self.page.get_by_test_id("descricao").fill(str(descricao))
            print("produto registado:", descricao)
            self.page.get_by_test_id("quantity").fill(str(quantidade))
            print("produto registado", quantidade)        
        
            if str(foto) == 'yes':
                assert IMAGE_PATH.exists(), "Image not found"
                self.page.set_input_files('[data-testid="imagem"]',IMAGE_PATH)
                # aguarda o frontend processar o upload
                self.page.wait_for_timeout(1000)
                submit = self.page.get_by_test_id("cadastarProdutos")
                expect(submit).to_be_visible()
                expect(submit).to_be_enabled()  
                submit.click()

            submit = self.page.get_by_test_id("cadastarProdutos")
            expect(submit).to_be_visible()
            expect(submit).to_be_enabled()              
            submit.click()
            self.page.wait_for_timeout(10000)
    