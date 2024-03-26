from typing import List
import time
import asyncio
import os

from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.callbacks import get_openai_callback
from src.settings import OPENAI_API_KEY

def get_chat_llm(config):
    return ChatOpenAI(openai_api_key=OPENAI_API_KEY)

def create_chat_llm_chain(system_template, user_template, system_variables, user_variables, config):
    prompt_system_message= SystemMessagePromptTemplate(
        prompt=PromptTemplate(template=system_template, input_variables=system_variables)
    )
    prompt_user_message= HumanMessagePromptTemplate(
        prompt=PromptTemplate(template=user_template, input_variables=user_variables)
    )
    llm = get_chat_llm(config=config)
    prompt = ChatPromptTemplate.from_messages([prompt_system_message,prompt_user_message])
    return LLMChain(llm=llm, prompt=prompt)

async def execute_chains_concurrently(input_data,input_chain):
    async def _execute_chain(data,chain):
        return await chain.arun(data)

    task_list = [_execute_chain(data_item, input_chain) for data_item in input_data] 
    return await asyncio.gather(*task_list, return_exceptions=True)

def make_openai_call(data,chain):
    s = time.perf_counter()
    print("OpenAI Call started")
    loop = asyncio.new_event_loop()
    with get_openai_callback() as cb:
        try:
            output_list = loop.run_until_complete(
                execute_chains_concurrently(data,chain)
            )
        finally:
            loop.close()
        time_taken = time.perf_counter()-s
    print(f"Time_taken: {time_taken:0.2f} seconds")
    print("Cost:\n",cb)
    return output_list