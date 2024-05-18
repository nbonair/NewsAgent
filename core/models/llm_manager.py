from core.models.llm import *
from core.models.llm import base
from core.models.llm.llm_openai import OpenAILLM
class LLMManager():
    def __init__(self):
        self.model = base.LLMBase()
        
    def get_llm(self, model = ''):
        if model == 'openai':
            self.model = OpenAILLM()
        else:
            raise ValueError(f'Unknown LLM model: {model}')
            
        return self.model
    
    def process_request(self, model, prompt: str) -> str:
        llm = self.get_llm(model)
        return llm.interact(prompt)