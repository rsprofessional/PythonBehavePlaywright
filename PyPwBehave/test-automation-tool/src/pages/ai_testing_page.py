from browser_use import Agent

from browser_use.llm import ChatGoogle



class AiDemo:

    async def gemini_ai_demo(self):

        task = """

        Open the website https://front.serverest.dev/cadastrarusuarios

        Fill the box Digite seu nome field with Raul Santos

        Fill the box Digite seu email with user1@email.com

        Fill the box Digite sua senha with 123456

        Click the register button

        Wait 5 seconds

        """



        llm = ChatGoogle(model="gemini-2.0-flash-exp", api_key="AIzaSyA1Sra2knspVf_ECLoJDKacpxaKGyW-vmA")



        agent = Agent(task=task, llm=llm)

        await agent.run()
