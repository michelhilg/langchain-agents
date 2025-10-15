from langchain.agents import AgentExecutor
from agente import AgenteOpenAIFunctions
from dotenv import load_dotenv

load_dotenv()

pergunta = "Quais os dados de Ana?"

agente = AgenteOpenAIFunctions()

executor = AgentExecutor(agent=agente.agente,
                        tools=agente.tools,
                        verbose=True)
resposta = executor.invoke({"input" : pergunta})
print(resposta)