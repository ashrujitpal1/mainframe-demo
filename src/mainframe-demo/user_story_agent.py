# agents/user_story_agent.py
from typing import Dict
from langchain.agents import Agent
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from tools.api_tools import UserStoryAPITool

class UserStoryAgent(Agent):
    def __init__(self):
        self.tools = [UserStoryAPITool()]
        
        self.prompt = PromptTemplate(
            template="""You are a User Story Generator Agent.
            Your task is to generate user stories based on the given topic.
            
            Topic: {topic}
            
            Generate detailed user stories and return them in JSON format.
            """,
            input_variables=["topic"]
        )

    async def process(self, topic: str) -> Dict[str, Any]:
        tool = self.tools[0]
        result = tool.run(topic)
        return result
