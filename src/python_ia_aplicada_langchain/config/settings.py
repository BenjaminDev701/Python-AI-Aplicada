"""Configuración del entorno"""
import os
from dotenv import load_dotenv

load_dotenv()


class LangchainSettings:
    CHAT_MODEL: str = os.getenv("OPEN_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Parámetros
    DEFAULT_TEMPERATURE: float = 0.7
    LOW_TEMPERATURE: float = 0.1
    MAX_RETRIES: int = 3

    # Rutas de Persistencia
    SQLITE_DB_PATH: str = "data/chat_history.db"
    CHROMA_PATH: str = "./data/langchain_chroma"

    # Configuración de RAG
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    TOP_K_RESULTS: int = 3

    # Costos dinámicos
    COST_INPUT_PER_MILLION: float = 0.15

    @classmethod
    def validate(cls) -> None:
        """Valida variables críticas"""
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError(
                "La variable de entorno OPENAI_API_KEY no está configurada"
            )


settings = LangchainSettings()
