"""Demo LCEL"""

from src.python_ia_aplicada_langchain.core.llm import get_llm
from src.python_ia_aplicada_langchain.config.settings import settings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = get_llm()


def demo_simple_chain() -> None:
    """Cadena Simple"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto en {tema}. Responde maximo 3 oraciones"),
        ("human", "{pregunta}")
    ])

    parser = StrOutputParser()

    chain = prompt | llm | parser

    respuesta = chain.invoke({
        "tema": "salario y futuro de un ia software engineer de 0 a 5 años",
        "pregunta": "¿Cual es el salario promedio de un ia software engineer de 0 a 5 años en mexico, , detallalo por año?"
    })

    print("Simple chain")
    print(respuesta)


if __name__ == "__main__":
    print("="*60)
    print("Langchain LCEL - Fundamentos")
    print("="*60)
    demo_simple_chain()
