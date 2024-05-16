from abc import ABC, abstractmethod


class LLMBase(ABC):
    @abstractmethod
    def interact(self, prompt: str) -> str:
        pass