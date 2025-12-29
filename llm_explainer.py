import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="groq/compound",
    temperature=0.3
)

def explain_graph(prompt: str) -> str:
    messages = [
        SystemMessage(
            content=(
                "You are a senior data analyst. "
                "Explain Olympic data visualizations clearly, "
                "concisely, and in simple language."
            )
        ),
        HumanMessage(content=prompt)
    ]
    response = llm.invoke(messages)
    return response.content
