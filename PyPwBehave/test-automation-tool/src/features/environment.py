from pages.common_page import OpenApplication
import os
from datetime import datetime


def before_all(context):
    print(">>> Antes de todos os testes")
    context.app = OpenApplication()
    context.app.launch_browser_and_open_page()

def after_all(context):
    print(">>> Depois de todos os testes")
    context.app.browser.close()


def after_step(context, step):
        if step.status == "failed":
            # cria pasta se não existir
            if not os.path.exists("reports/screenshots"):
                os.makedirs("reports/screenshots")

            screenshot_file = f"reports/screenshots/{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            context.page.screenshot(path=screenshot_file)
            print(f"Screenshot capturada: {screenshot_file}")

