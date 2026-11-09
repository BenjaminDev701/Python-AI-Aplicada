"""Cliente centralizado"""

from tiktoken import model
from functools import lru_cache
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from src.python_ia_aplicada_langchain.config.settings import settings


# es para que guardo un resultado en el cache
@lru_cache(maxsize=1)
def get_llm(temperature: float = None) -> ChatOpenAI:
    """Retorna Cliente MLL"""
    return ChatOpenAI(
        model=settings.CHAT_MODEL,
        temperature=temperature or settings.DEFAULT_TEMPERATURE,
        max_retries=settings.MAX_RETRIES
    )


@lru_cache(maxsize=1)
def get_embeddings() -> OpenAIEmbeddings:
    """Retorna el cliente de embeddings"""
    return OpenAIEmbeddings(
        model=settings.EMBEDDING_MODEL
    )
