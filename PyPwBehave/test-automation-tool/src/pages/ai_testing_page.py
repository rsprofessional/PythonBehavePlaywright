from browser_use import Agent

from browser_use.llm import ChatGoogle




class AiDemo:

    async def gemini_ai_demo(self):

        task = """
        Go to https://front.serverest.dev/cadastrarusuarios
        Find the input field for 'Nome' and type 'Raul Santos'
        Find the input field for 'Email' and type 'raul_teste_123@email.com'
        Find the input field for 'Senha' and type '123456'
        Click the button 'Cadastrar'
        Wait for the success message or for the page to change
        """



        llm = ChatGoogle(model="gemini-2.0-flash-exp", api_key="AIzaSyA1Sra2knspVf_ECLoJDKacpxaKGyW-vmA")



        agent = Agent(task=task, llm=llm)

        await agent.run()
