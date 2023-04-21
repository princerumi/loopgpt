from loopgpt.models.llama_cpp import LlamaCppModel
from loopgpt.models.openai_ import OpenAIModel
from loopgpt.models.base import *


user_providers = {}


def register_model_type(provider):
    if isinstance(provider, BaseConversationModel):
        provider = provider.__class__
    if not isinstance(provider, type):
        raise TypeError(f"{provider} is not a class")
    if not issubclass(provider, BaseConversationModel):
        raise TypeError(f"{provider} does not inherit from ConversationalModelBase")
    user_providers[provider.__name__] = provider


def from_config(config) -> BaseConversationModel:
    class_name = config["class"]
    clss = user_providers.get(class_name) or globals()[class_name]
    return clss.from_config(config)
