
"""Configuracion del entorno"""
import os
from dotenv import load_dotenv

load_dotenv()


class LangchainSettings:
    CHAT_MODEL = str = os.environ["OPEN_MODEL", "gpt-4o-mini"]
    EMBEDDING_MODEL: str = "text-embedding-3-small"


# Parametros
    DEFAULT_TEMPERATURE: float = 0.7
    LOW_TEMPERATURE: float = 0.1
    MAX_RETRIES: int = 3

# Rutas de Persisntencia
    SQLITE_DB_PATH: str = "data/chat_history.db"
    CHROMA_PATH: str = "./data/langchain_chroma"


# Configuracion de RAG
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    TOP_K_RESULTS: int = 3

# Costos dinamicos
    COST_INPUT_PER_MOLLION = float = 0.15


@classmethod
def validate(cls) -> None:
    """Valida variables criticas"""
    if not os.getenv("OPEN_API_KEY"):
        raise ValueError(
            "Variable de OPEN_API_KEY no esta configurada"
        )


settings = LangchainSettings()
