from langchain.chains.summarize import load_summarize_chain
from models.llm_manager import LLMManager


class AgentSummarization:
    def __init__(self, model="openai"):
        self.llm_manager = LLMManager()
        self.llm = self.llm_manager.get_llm(model)
        self.chain = load_summarize_chain(self.llm)

    def summarize_text(self, text):
        summary = self.chain(text)
        return summary['output_text']
