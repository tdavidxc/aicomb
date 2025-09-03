#the base class for llm clients
#03/09/2025 working on the backend

from abc import ABC, abstractmethod #python method to make abstract classes

class LLMClient(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key #storing the api key within the class

    @abstractmethod
    def send_message(self, prompt: str, history: list, settings: dict):
        #sending a prompt to the llm and returning the response
        pass

    @abstractmethod
    def get_models(self):
        #returning a list of available models for the llm
        pass

    @abstractmethod
    def stream_response(self, prompt: str, history: list, settings: dict):
        #streaming the response from the llm
        yield from []

    @abstractmethod
    def test_connection(self) -> bool:
        #testing the connection to the llm service with a boolean flag
        return True