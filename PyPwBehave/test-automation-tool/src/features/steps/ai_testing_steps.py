from behave import *
from pages.ai_testing_page import AiDemo
import asyncio

agent_ai = AiDemo()

@Given('Acess the website and make login')
def step_impl(context):
    asyncio.run(agent_ai.gemini_ai_demo())
